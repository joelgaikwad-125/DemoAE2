# Base Class (Parent)
class Animal:
    def _init_(self, name):
        self.name = name

    def speak(self):
        return "Animal makes a sound. HAHAHAHAHAHAHAHAHHAHAHHAHA"

# Derived Class 1 (Child of Animal)
class TATYA(Animal):
    def _init_(self, name, color):
        super()._init_(name)
        self.color = color

    def speak(self):
        return f"{self.name} (a {self.breed}) barks!"

# Derived Class 2 (Child of Animal)
class Cat(Animal):
    def _init_(self, name, color):
        super()._init_(name)
        self.color = color

    def speak(self):
        return f"{self.name} (a {self.color} Pussy cat) meows!"

# Derived Class 3 (Child of Animal)
class Bird(Animal):
    def __init__(self, name, species, wing_span):
        super().__init__(name)
        self.species = species
        self.wing_span = wing_span  # Additional attribute

    def speak(self):
        return f"{self.name} (a {self.species}) chirps!"

    def fly(self, distance):
        return f"{self.name} flies {distance} meters!"

    def eat(self, food):
        return f"{self.name} pecks at some {food}."

    def describe(self):
        return f"{self.name} is a {self.species} with a wingspan of {self.wing_span} meters."


# Creating objects and calling methods

TATYA = TATYA("Buddy", "Gold yelow")
cat = Cat("Whiskers", "Black")

cat = Cat("Kali Billi", "Black")

bird = Bird("Charlie", "Parrot")

# Displaying output
print(TATYA.speak())   # Buddy (a Golden Retriever) barks!
print(cat.speak())   # Whiskers (a Black cat) meows!
print(bird.speak())  # Charlie (a Parrot) chirps!
