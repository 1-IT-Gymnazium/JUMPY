"""
This module handles the creation, management, and rendering of tilemaps for
the game. It provides functionalities
for loading and saving tilemaps from files, accessing and modifying the tiles
 within the map, and rendering the
tilemap to the screen. It also includes utilities for tile-based collision
detection and automatic tile variant
selection based on neighboring tiles to create more visually cohesive maps.
"""

import json
import pygame


NEIGHBOR_OFFSETS = [
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (1, 0),
    (0, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]

tiles_set = {"grass", "stone", "sky"}


class Tilemap:
    """
    Manages a grid of tiles for the game world, including loading, saving,
    rendering, and collision detection.

    Attributes:
        game (Game): The main game object, providing access to global
        resources and settings.
        tile_size (int): The size of each tile in pixels.
        tilemap (dict): A dictionary representing the grid of tiles, with
        keys as string coordinates "x;y".
        offgrid_tiles (list): A list of tiles that do not align to the grid,
        used for decorative elements.
    """

    def __init__(self, game, tile_size=16):
        """
        Initializes a new Tilemap instance.

        Parameters:
            game (Game): The main game object.
            tile_size (int, optional): The size of each tile in pixels.
            Defaults to 16.
        """
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

    def extract(self, id_pairs, keep=False):
        """
        Extracts tiles from the map matching specific id and variant pairs.

        Parameters:
            id_pairs (list of tuple): A list of tuples (type, variant)
            to match tiles against.
            keep (bool, optional): Whether to keep the matched tiles in the
            map. Defaults to False.

        Returns:
            list: A list of matched tiles with their properties.
        """
        matches = []

        for tile in self.offgrid_tiles.copy():
            if (tile["type"], tile["variant"]) in id_pairs:
                matches.append(tile.copy())
                if not keep:
                    self.offgrid_tiles.remove(tile)

        for loc in list(self.tilemap.keys()):
            tile = self.tilemap[loc]
            if (tile["type"], tile["variant"]) in id_pairs:
                matches.append(tile.copy())
                matches[-1]["pos"] = matches[-1]["pos"].copy()
                matches[-1]["pos"][0] *= self.tile_size
                matches[-1]["pos"][1] *= self.tile_size
                if not keep:
                    del self.tilemap[loc]

        return matches

    def tiles_around(self, pos):
        """
        Gets a list of tiles surrounding a specific position.

        Parameters:
            pos (tuple): The position to check around, in pixels.

        Returns:
            list: A list of tiles around the specified position.
        """
        tiles = []
        tile_loc = (
            int(pos[0] // self.tile_size),
            int(pos[1] // self.tile_size),
        )

        for offset in NEIGHBOR_OFFSETS:
            check_loc = (
                str(tile_loc[0] + offset[0])
                + ";"
                + str(tile_loc[1] + offset[1])
            )
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles

    def save(self, path):
        """
        Saves the current state of the tilemap to a file.

        Parameters:
            path (str): The file path to save the tilemap to.
        """
        with open(path, "w") as f:
            json.dump(
                {
                    "tilemap": self.tilemap,
                    "tile_size": self.tile_size,
                    "offgrid": self.offgrid_tiles,
                },
                f,
            )

    def load(self, path):
        """
        Loads a tilemap from a file, replacing the current state.

        Parameters:
        path (str): The file path to load the tilemap from.
        """
        with open(path, "r") as f:
            map_data = json.load(f)

        if "level" in map_data:
            map_data["level"] = min(map_data["level"], 2)
        if "entity_count" in map_data:
            map_data["entity_count"] = min(map_data["entity_count"], 2)

        self.tilemap = map_data["tilemap"]
        self.tile_size = map_data["tile_size"]
        self.offgrid_tiles = map_data["offgrid"]

    def solid_check(self, pos):
        """
        Checks if a given position collides with a solid tile.

        Parameters:
            pos (tuple): The position to check, in pixels.

        Returns:
            bool: True if there is a collision with a solid tile, False
              otherwise.
        """
        tile_loc = (
            str(int(pos[0] // self.tile_size))
            + ";"
            + str(int(pos[1] // self.tile_size))
        )
        if tile_loc in self.tilemap:
            if self.tilemap[tile_loc]["type"] in tiles_set:
                return self.tilemap[tile_loc]

    def physics_rects_around(self, pos):
        """
        Gets a list of pygame.Rect objects for solid tiles around a
        specified position, for physics calculations.

        Parameters:
            pos (tuple): The position to check around, in pixels.

        Returns:
            list: A list of pygame.Rect objects for solid tiles around
            the specified position.
        """
        rects = []
        for tile in self.tiles_around(pos):
            if tile["type"] in tiles_set:
                rects.append(
                    pygame.Rect(
                        tile["pos"][0] * self.tile_size,
                        tile["pos"][1] * self.tile_size,
                        self.tile_size,
                        self.tile_size,
                    )
                )
        return rects

    def render(self, surf, offset=(0, 0)):
        """
        Renders the tilemap onto a given surface.

        Parameters:
            surf (pygame.Surface): The surface to render the tilemap on.
            offset (tuple): An (x, y) offset to apply to the tile positions,
            used for camera movement.
        """
        for tile in self.offgrid_tiles:
            surf.blit(
                self.game.assets[tile["type"]][tile["variant"]],
                (tile["pos"][0] - offset[0], tile["pos"][1] - offset[1]),
            )

        for x in range(
            offset[0] // self.tile_size,
            (offset[0] + surf.get_width()) // self.tile_size + 1,
        ):
            for y in range(
                offset[1] // self.tile_size,
                (offset[1] + surf.get_height()) // self.tile_size + 1,
            ):
                loc = str(x) + ";" + str(y)
                if loc in self.tilemap:
                    tile = self.tilemap[loc]
                    surf.blit(
                        self.game.assets[tile["type"]][tile["variant"]],
                        (
                            tile["pos"][0] * self.tile_size - offset[0],
                            tile["pos"][1] * self.tile_size - offset[1],
                        ),
                    )
