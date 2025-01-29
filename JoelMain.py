# Base Class (Parent)
class Animal:
    def _init_(self, name):
        self.name = name

    def speak(self):
        return "Animal makes a sound."

# Derived Class 1 (Child of Animal)
class Dog(Animal):
    def _init_(self, name, breed):
        super()._init_(name)
        self.breed = breed

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
    def _init_(self, name, species):
        super()._init_(name)
        self.species = species

    def speak(self):
        return f"{self.name} (a {self.species}) chirps!"

# Creating objects and calling methods
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Kali Billi", "Black")
bird = Bird("Charlie", "Parrot")

# Displaying output
print(dog.speak())   # Buddy (a Golden Retriever) barks!
print(cat.speak())   # Whiskers (a Black cat) meows!
print(bird.speak())  # Charlie (a Parrot) chirps!
