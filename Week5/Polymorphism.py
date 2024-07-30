class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def let_it_fly(obj):
    obj.fly()

bird = Bird()
airplane = Airplane()

let_it_fly(bird)  # Output: Bird is flying
let_it_fly(airplane)  # Output: Airplane is flying
