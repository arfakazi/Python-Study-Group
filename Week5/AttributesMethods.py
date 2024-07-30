class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} is barking!"

    # Class method
    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

    # Another instance method
    def birthday(self):
        self.age += 1
        return f"Happy Birthday {self.name}! You are now {self.age} years old."

# Create an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Access class attribute
print(f"Species: {Dog.species}")  # Output: Species: Canis familiaris

# Access instance attributes
print(f"Name: {my_dog.name}")  # Output: Name: Buddy
print(f"Age: {my_dog.age}")  # Output: Age: 3

# Call instance method
print(my_dog.bark())  # Output: Buddy is barking!

# Call class method to change class attribute
Dog.change_species("Canis lupus")
print(f"New Species: {Dog.species}")  # Output: New Species: Canis lupus

# Call another instance method
print(my_dog.birthday())  # Output: Happy Birthday Buddy! You are now 4 years old.
