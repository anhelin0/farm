# Farm Animal Simulation

A GUI-based farm animal simulation game where you can take care of various farm animals. The game allows you to manage individual animals or the entire group, breed new animals, and monitor their health, hunger, and boredom levels.

## Features

- 🖥️ Modern GUI interface with intuitive controls
- 🐄 Multiple animal types (Cow, Chicken, Sheep, Pig, Horse)
- 🎮 Individual and group animal care options
- 👶 Animal breeding system
- 📊 Real-time status updates
- 🎲 Random initial states for each animal
- ❤️ Health, hunger, and boredom management
- ⏯️ Game pause/resume functionality

## Requirements

- Python 3.x
- tkinter (usually comes with Python)
- sphinx (for documentation)
- sphinx-rtd-theme (for documentation theme)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/farm-simulation.git
cd farm-simulation
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

## Running the Game

To start the game, run:
```bash
python farm_gui.py
```

## How to Play

1. When you start the game, you'll see a list of animals and their current status
2. Click the "Start Game" button to begin the simulation
3. Use the control buttons to:
   - Feed individual animals (select an animal first)
   - Play with individual animals (select an animal first)
   - Feed all animals at once
   - Play with all animals at once
   - Breed specific types of animals
4. Monitor animal status in the main display
5. Status messages will appear in the bottom text area

## Game Mechanics

- Animals' hunger and boredom increase over time
- If hunger or boredom reaches 100%, health decreases
- Animals die if health reaches 0
- Feeding reduces hunger but increases boredom
- Playing reduces boredom but increases hunger
- Breeding requires at least 2 animals of the same type

## Project Structure

- `animal.py`: Base Animal class with core functionality
- `farm_animals.py`: Specific animal type implementations
- `farm.py`: Farm management class
- `farm_gui.py`: GUI implementation
- `requirements.txt`: Project dependencies
- `docs/`: Documentation files
- `LICENSE`: MIT License

## Documentation

To generate the documentation:
```bash
cd docs
make html
```

The documentation will be available in `docs/_build/html/`.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to all contributors
- Inspired by classic farm simulation games
- Built with Python and tkinter 