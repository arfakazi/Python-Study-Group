class Parent:          # Parent Class
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, {self.name}"
    
class Child(Parent):          # Child Class
    def play(self):         # Method in child class
        return f"{self.name} is playing!"   # Attribute from parent class
