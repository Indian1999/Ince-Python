from classes.animal import Animal
class Mammal(Animal):
    def __init__(self, name = "defaultMammal", age = 0, weight = None, male = True, fur_color = "black"):
        super().__init__(name, age, weight, male)
        self.fur_color = fur_color
    
    def __str__(self):
        gender = "Male" if self.male else "Female"
        return f"(name = {self.name}, age = {self.age}, weight = {self.weight}, {gender}, fur color = {self.fur_color})"