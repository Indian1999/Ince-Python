from classes.mammal import Mammal

class Dog(Mammal):
    def __init__(self, name = "defaultDog", age = 0, weight = None, male = True, fur_color = "black"):
        super().__init__(name, age, weight, male, fur_color)

    def make_noise(self):
        print("Vau")