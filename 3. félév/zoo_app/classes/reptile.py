from classes.animal import Animal
class Reptile(Animal):
    def __init__(self, name = "defaultMammal", age = 0, weight = None, male = True, venomous = False):
        super().__init__(name, age, weight, male)
        self.venomous = venomous
    
    def __str__(self):
        gender = "Male" if self.male else "Female"
        venomous = "Venomous" if self.venomous else "Not venomous"
        return f"(name = {self.name}, age = {self.age}, weight = {self.weight}, {gender}, {venomous})"
