class Dog:
    def __init__(self, name, age): # CONSTRUCTOR METHOD
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")

# Creating an object of the Dog class
my_dog = Dog("Buddy", 3)
my_dog2 = Dog("Tommy", 5)
#print(my_dog.name)  # Output: Buddy
#my_dog2.bark()  # Output: Buddy is barking!
print(my_dog.age)
