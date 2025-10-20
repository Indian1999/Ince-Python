from classes.mammal import Mammal

class Lion(Mammal):
    def __init__(self, name = "defaultLion", age = 0, weight = None, male = True, fur_color = "brown"):
        super().__init__(name, age, weight, male, fur_color)

    def make_noise(self):
        print("Roarrrr")