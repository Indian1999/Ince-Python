import random

class Car:
    def __init__(self, rendszam, loero, ajtok_szama, márka, évjárat):
        self.rendszam = rendszam
        self.loero = loero
        self.ajtok_szama = ajtok_szama
        self.márka = márka
        self.évjárat = évjárat

    def __str__(self):
        return f"{self.rendszam} - {self.márka} ({self.évjárat}), HP: {self.loero}, Doors: {self.ajtok_szama}"
    
class Garage:
    def __init__(self, name, car_list, capacity):
        self.name = name
        self.car_list = car_list
        self.capacity = capacity

    def park(self, car):
        if self.capacity > len(self.car_list):
            self.car_list.append(car)

    def num_of_cars(self):
        return len(self.car_list)

    def fullness(self):
        return self.num_of_cars() / self.capacity * 100    
    
    def __str__(self):
        return f"{self.name} - {self.num_of_cars()}/{self.capacity} ({ round(self.fullness()) }%)"
    
    def is_full(self):
        return len(self.car_list) == self.capacity


parkoló1 = Garage("Parkoló 1", [], 92)
parkoló2 = Garage("Parkoló 2", [], 82)

f = open("input.txt", "r", encoding="utf-8")
for line in f:
    #line = "UNT-647;120;2;Honda;2023"
    items = line.split(";") # -> ["UNT-647", "120", "2", "Honda", "2023"]
    car = Car(items[0], int(items[1]), int(items[2]), items[3], int(items[4]))
    rnd = random.randint(1,2)
    if rnd == 1 and not parkoló1.is_full():
        parkoló1.park(car)
    else:
        parkoló2.park(car)
    
f.close()

print(parkoló1)
print(parkoló2)

# 1. feladat: Melyik parkolóban van több kocsi?
if parkoló1.num_of_cars() > parkoló2.num_of_cars():
    print("Parkoló1-ben van több autó")
elif parkoló1.num_of_cars() < parkoló2.num_of_cars():
    print("Parkoló2-ben van több autó")
else:
    print("Azonos számú autó van mindkét parkolóban.")

# 2. feladat: Melyik parkolóban nagyobb a telítettség (%-os érték)?
if parkoló1.fullness() > parkoló2.fullness():
    print("Parkoló1 van nagyobb %-ban tele.")
elif parkoló1.fullness() < parkoló2.fullness():
    print("Parkoló2 van nagyobb %-ban tele.")
else:
    print("Azonos százalékig telítettek a parkolók.")

# 3. feladat: Mennyi az átlagos lóerő a parkoló 2-ben?

# 4. feladat: Írjuk ki a legöregebb kocsi adatait (mindegy melyik parkolóból)

# 5. feladat: Hány db 2005-ös évjáratú kocsi van a 2-es parkolóban?

# 6. feladat: Parkoló2 be fog zárzni, de szerencsére Parkoló1-hez hozzáépítenek még egy 50 ferőhelyes emeletet. Mozgassuk át az összes kocsit Parkoló2-ből Parkoló1-be!

# 7. feladat: Mennyi a Trabant autók átlagos lóereje?

# 8. feladat: Melyik típusú autóból található a legtöbb?