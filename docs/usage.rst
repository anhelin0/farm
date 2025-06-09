Usage Guide
==========

This guide explains how to play and use the Farm Animal Simulation game.

Getting Started
-------------

1. Launch the game:
   .. code-block:: bash

      python farm_gui.py

2. You'll see the main game window with:
   * List of animals
   * Control buttons
   * Status display

Game Interface
------------

The game interface consists of three main sections:

1. Animal List
   * Shows all animals on the farm
   * Displays name, type, hunger, boredom, health, age, and status
   * Click on an animal to select it

2. Control Panel
   * Start/Pause Game button
   * Individual Care options
   * Group Care options
   * Breeding options
   * Add New Animal button

3. Status Display
   * Shows game messages
   * Displays animal status updates
   * Shows breeding results

Game Controls
-----------

Individual Animal Care
~~~~~~~~~~~~~~~~~~~~

1. Select an animal from the list
2. Use "Feed Selected" to feed the animal
3. Use "Play with Selected" to play with the animal

Group Care
~~~~~~~~~

1. Use "Feed All" to feed all animals
2. Use "Play with All" to play with all animals

Breeding
~~~~~~~

1. Click on a breeding button (e.g., "Cows")
2. If you have at least 2 animals of that type, a new animal will be born
3. The new animal will appear in the list

Adding New Animals
~~~~~~~~~~~~~~~

1. Click "Add New Animal"
2. Select the animal type
3. Click "Add Animal"

Game Mechanics
------------

Animal States
~~~~~~~~~~~

* **Hunger**: Increases over time, decreases when fed
* **Boredom**: Increases over time, decreases when played with
* **Health**: Decreases if hunger or boredom reaches 100%
* **Age**: Increases each day

Animal Care
~~~~~~~~~

* Feeding reduces hunger but increases boredom
* Playing reduces boredom but increases hunger
* Animals die if health reaches 0

Tips
----

* Monitor animal status regularly
* Balance feeding and playing
* Keep at least 2 animals of each type for breeding
* Use the pause button when needed
* Check status messages for important updates 