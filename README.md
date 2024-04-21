# JUMPY!

Welcome to the GitHub repository for "JUMPY!", an engaging and visually stunning 2D pixel art platformer. In this game, players navigate through multiple unique levels, each meticulously crafted to offer a distinct challenge with beautiful graphical themes. Travel from the depths of mystic caves to the tops of towering mountains, passing through lush green landscapes along the way.

## Game Features

- **Varied Levels**: Embark on a journey from the dark, intricate caverns to the majestic peaks of mountains, each level brimming with unique aesthetics and challenges.
- **Enemies and Traps**: Battle against mages wielding magical powers and avoid natural traps such as spikes, stalactites, and stalagmites that add danger to your adventure.
- **Stunning Pixel Art**: Experience beautifully crafted pixel art that brings the game's varied worlds to life with vibrant colors and detailed textures.

## Installation

1. **Download**: Fetch `JUMPY!.zip` from the releases section.
2. **Unzip**: Extract the contents into a designated folder.
3. **Dependencies**: Ensure all required dependencies are installed.
4. **Launch**: Execute `JUMPY!.exe` to begin your adventure.

## How to Play

- **Movement**: Use `A` and `D` keys to move left and right.
- **Jump**: Press `SPACE` to leap over obstacles.
- **Attack**: Press `X` to attack.
- **Avoid Hazards**: Steer clear of spikes, falling stalactites, and sharp stalagmites.
- **Objective**: Reach the end of each level, from 1 to 3.

## File Structure

- `main.py`: Not uploaded. If available, it should initialize and launch the game, setting up the main game window and session.
- `game.py`: Central hub for the game loop and state management, coordinating gameplay mechanics and handling transitions between different states.
- `entities.py`: Defines player and enemy classes, managing character behaviors, abilities, and interactions within the game.
- `utils.py`: Provides utility functions that assist with collision handling, score management, and other supportive functionalities.
- `tilemap.py`: Manages the tile-based maps used in the game, including the layout of tiles and collision properties.
- `clouds.py`: Handles the rendering and animation of background elements like clouds, enhancing the visual appeal of the game environment.
- `particle.py`: Manages particle effects, such as explosions, collisions, or other visual effects associated with gameplay interactions.

### Graphics/
- **Contained in a data folder**: Includes sprite sheets, background images, and other visual assets in PNG format. These are crucial for the visual representation of all game elements.

### Sounds/
- **Contained in a data folder**: Includes all sound effects and music files.
  - `music.wav`: Background music file.
  - **SFX folder**: Contains individual sound effect files for various game actions and interactions.

### Levels/
- **Contained in the data/map folder**: Each level is stored as a JSON file, detailing the layout, entities, and game mechanics specific to that level.

## Dependencies
To ensure a smooth gameplay experience, install the following:

- **Python 3.12**: Download and install from the official Python website.
- **Pygame**: A robust library for writing video games in Python.

```bash
pip install pygame
```

---
