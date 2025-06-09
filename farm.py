from farm_animals import Cow, Chicken, Sheep, Pig, Horse
import random

class Farm:
    """
    Farm class that manages all animals.
    Handles adding, removing, and caring for animals.
    """
    def __init__(self):
        # List to store all animals on the farm
        self.animals = []
        # Create initial animals when farm is created
        self.initialize_farm()

    def initialize_farm(self):
        """Create initial animals for the farm (at least 5)"""
        # List of all possible animal types
        animal_classes = [Cow, Chicken, Sheep, Pig, Horse]
        total_animals = 0
        
        # Keep adding animals until we have at least 5
        while total_animals < 5:
            # Pick a random animal type
            animal_class = random.choice(animal_classes)
            # Create 1-3 animals of this type
            num_to_create = random.randint(1, 3)
            
            for i in range(num_to_create):
                name = f"{animal_class.__name__}{total_animals + 1}"
                self.animals.append(animal_class(name))
                total_animals += 1

    def add_animal(self, animal):
        """Add a new animal to the farm"""
        self.animals.append(animal)

    def remove_animal(self, animal):
        """Remove an animal from the farm"""
        if animal in self.animals:
            self.animals.remove(animal)

    def feed_all(self):
        """Feed all alive animals on the farm"""
        messages = []
        for animal in self.animals:
            if animal.is_alive:
                messages.append(animal.feed())
        return messages

    def play_with_all(self):
        """Play with all alive animals on the farm"""
        messages = []
        for animal in self.animals:
            if animal.is_alive:
                messages.append(animal.play())
        return messages

    def update_all(self):
        """Update all animals' states (called each day)"""
        messages = []
        for animal in self.animals:
            message = animal.update()
            if message:
                messages.append(message)
        return messages

    def get_all_status(self):
        """Get status of all animals"""
        return [animal.get_status() for animal in self.animals]

    def get_animal_count(self, animal_type):
        """Count how many alive animals of a specific type we have"""
        return len([a for a in self.animals if isinstance(a, animal_type) and a.is_alive])

    def breed_animals(self, animal_type):
        """Try to breed two animals of the same type"""
        # Get all alive animals of the requested type
        animals_of_type = [a for a in self.animals if isinstance(a, animal_type) and a.is_alive]
        count = len(animals_of_type)
        
        # Need at least 2 animals to breed
        if count >= 2:
            # Pick two random parents
            parent1, parent2 = random.sample(animals_of_type, 2)
            # Create a new baby animal
            new_animal = animal_type(f"Baby{animal_type.__name__}{len(self.animals) + 1}")
            self.add_animal(new_animal)
            return f"New {animal_type.__name__} born! Total {animal_type.__name__}s: {count + 1}"
        else:
            return f"Need at least 2 {animal_type.__name__}s to breed. Current count: {count}" 