# Let's make a car class
class Car:
    garageName= "Arfa's garage"
    
    def __init__(self, make, model, year, color): #Class constructor
        self.make = make
        self.__model = model #private
        self.year = year
        self.color = color
    
    def tell_color(self):
        print(f"The color of {self.model} is {self.color}")

car1 = Car("Nissan", "Sunny", 2008, "white")
car1.tell_color()
print(car1.model)
#print(car1)