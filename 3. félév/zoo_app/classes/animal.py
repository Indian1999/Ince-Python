class Animal:
    def __init__(self, name = "defaultName", age = 0, weight = None, male = True):
        self.name = name
        self.age = age
        self.weight = weight
        self.male = male

    def make_noise(self):
        print("Make generic noise.")

    def __str__(self):
        gender = "Male" if self.male else "Female"
        return f"(name = {self.name}, age = {self.age}, weight = {self.weight}, {gender})"
