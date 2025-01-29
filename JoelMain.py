# Base Class (Parent)
class Animal:
    def _init_(self, name):
        self.name = name

    def speak(self):
        return "Animal makes a sound."

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
        return f"{self.name} (a {self.color} cat) meows!"

# Derived Class 3 (Child of Animal)
class Bird(Animal):
    def _init_(self, name, species):
        super()._init_(name)
        self.species = species

    def speak(self):
        return f"{self.name} (a {self.species}) chirps!"

# Creating objects and calling methods
TATYA = TATYA("Buddy", "Gold yelow")
cat = Cat("Whiskers", "Black")
bird = Bird("Charlie", "Parrot")

# Displaying output
print(TATYA.speak())   # Buddy (a Golden Retriever) barks!
print(cat.speak())   # Whiskers (a Black cat) meows!
print(bird.speak())  # Charlie (a Parrot) chirps!
