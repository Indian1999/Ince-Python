from classes.bird import Bird
from classes.dog import Dog
from classes.lion import Lion
from classes.reptile import Reptile

állatok = []

állatok.append(Dog("Buksi", 4, 13, True, "fekete"))
állatok.append(Bird("Csőri", 1, 0.2, False, 32))
állatok.append(Lion("Szimba", 2, 57, True, "zsemle"))
állatok.append(Reptile())

for állat in állatok:
    print(állat)
    állat.make_noise()

