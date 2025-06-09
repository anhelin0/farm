import random

class Animal:
    """
    Base class for all farm animals.
    This class handles the basic properties and behaviors of animals.
    """
    def __init__(self, name):
        # Initialize animal properties
        self.name = name
        # Random starting values between 0 and 100
        self.hunger = random.randint(0, 100)  # How hungry the animal is (0-100)
        self.boredom = random.randint(0, 100)  # How bored the animal is (0-100)
        self.health = 100  # Animal starts with full health
        self.age = 0  # Animal starts at 0 days old
        self.is_alive = True  # Animal starts alive

    def feed(self):
        """
        Feed the animal to reduce hunger and increase health.
        Returns a message about the feeding result.
        """
        if self.is_alive:
            # Reduce hunger by 30 points, but not below 0
            self.hunger = max(0, self.hunger - 30)
            # Increase health by 5 points, but not above 100
            self.health = min(100, self.health + 5)
            return f"{self.name} has been fed. Hunger level: {self.hunger}%"
        return f"{self.name} is no longer alive."

    def play(self):
        """
        Play with the animal to reduce boredom.
        Playing increases hunger slightly.
        Returns a message about the play result.
        """
        if self.is_alive:
            # Reduce boredom by 30 points, but not below 0
            self.boredom = max(0, self.boredom - 30)
            # Increase hunger by 10 points, but not above 100
            self.hunger = min(100, self.hunger + 10)
            return f"{self.name} has played. Boredom level: {self.boredom}%"
        return f"{self.name} is no longer alive."

    def update(self):
        """
        Update animal's state each day.
        Increases hunger and boredom, and checks health.
        Returns a message if the animal dies.
        """
        if self.is_alive:
            # Random increase in hunger and boredom each day
            self.hunger = min(100, self.hunger + random.randint(5, 15))
            self.boredom = min(100, self.boredom + random.randint(5, 15))
            self.age += 1  # Animal gets one day older
            
            # If animal is too hungry or bored, health decreases
            if self.hunger >= 100 or self.boredom >= 100:
                self.health -= 20
                
            # If health reaches 0, animal dies
            if self.health <= 0:
                self.is_alive = False
                return f"{self.name} has passed away."
        return None

    def get_status(self):
        """
        Get the current status of the animal.
        Returns a dictionary with all animal properties.
        """
        return {
            "name": self.name,
            "hunger": self.hunger,
            "boredom": self.boredom,
            "health": self.health,
            "age": self.age,
            "is_alive": self.is_alive
        }
