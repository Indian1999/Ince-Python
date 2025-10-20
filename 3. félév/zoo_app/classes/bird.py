from classes.animal import Animal
class Bird(Animal):
    def __init__(self, name = "defaultMammal", age = 0, weight = None, male = True, wingspan = 30):
        super().__init__(name, age, weight, male)
        self.wingspan = wingspan
    
    def __str__(self):
        gender = "Male" if self.male else "Female"
        return f"(name = {self.name}, age = {self.age}, weight = {self.weight}, {gender}, wingspan = {self.wingspan})"