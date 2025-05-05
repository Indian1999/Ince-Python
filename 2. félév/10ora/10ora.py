"""
# read függvény

file = open("2. félév/10ora/input.txt", "r", encoding="utf-8")
print(type(file)) # <class '_io.TextIOWrapper'>
print(file)       # <_io.TextIOWrapper name='2. félév/10ora/input.txt' mode='r' encoding='utf-8'>

print(file.read(10)) # Egyszer vo
print(file.read(10)) # lt, hol ne
print(file.read(500))
print(file.read(500))

# A read függvény az olvasófej aktuális állásától n karaktert fog beolvasni
# Vagy egészen EOF-ig (Tehát ha nincs n darab karakter, akkor a file végéig)
# EOF = End Of File

# Ha egy file-al már nem dolgozunk, akkor mindig zárjuk be!
file.close()
############################################################################
f = open("2. félév/10ora/input.txt", "r", encoding="utf-8")

for line in f:
    print(line)

f.close()

############################################################################
f = open("2. félév/10ora/input.txt", "r", encoding="utf-8")
print(f.read(5))
f.seek(2)
print(f.read(3))
f.seek(0)

lista = f.readlines() # Egy stringek listájaként visszaadja a file összes sorát
print(lista)
# Azt viszont fontos megfigyelni, hogy a \n-t a végén otthagyja (enter)
f.close()
"""
############################################################################

f = open("2. félév/10ora/hello_file_management.txt", "w", encoding="utf-8")
f.write("Kiskacsa fürdik. ")
f.write("Almafa")
f.write("\nHello World!")
f.writelines(["cica\n", "kutya\n", "elefánt\n", "majom"])

f.close()
###################################################################
f = open("2. félév/10ora/input.txt", "a", encoding="utf-8")
f.write("\nJajj de jó mese volt ez!")

# A w móddal vigyázni kell, mert ha létezik a file amit meg akarunk nyitni, akkor 
# annak a tartralmát teljesen törölni fogja
f.close()
##########################################################
f = open("2. félév/10ora/input.txt", "r+", encoding="utf-8")
print(f.read(40))
f.write("IDERONDÍTOK")

f.close()

# File megynitás módok:

# r - read ( csak olvasni tudjuk a filet) # olvasófej az elejéről
# w - write (csak írni tudunk bele, de fontos, hogy törlödik a megnyitott file tartalma megnyitáskor)
# a - append (csak írni tudunk bele, de nem törlődik a file tartalma megnyitáskor)
# az olvasófej a file végéről indul
# + írni és olvasni is tudunk

adatok = []
with open("2. félév/10ora/adatok.csv", "r", encoding="utf-8") as f:
    for line in f:
        adatok.append(line.strip().split(";"))
        # line = "Adam;13;Football\n"
        # line.strip() -> "Adam;13;Football"
        # "Adam;13;Football".split(";") -> ["Adam", "13", "Football"]
# Ha kiértünk a context managerből (with), akkor be is zárja file
print(adatok)


# Generáljunk autokat egy csv fileba
import random

def random_rendszám():
    betűk = "ABCDEFGHIJKLMNOPQRSTUVW"
    számok = "0123456789"
    rendszam = ""
    for i in range(3):
        rendszam += random.choice(betűk)
    rendszam += "-"
    for i in range(3):
        rendszam += random.choice(számok)
    return rendszam

márkák = ["Opel", "BMW", "Mercedes", "Renault", "Peugeot", "Kia", "Honda", "Toyota", "Tesla", "Skoda", "Wolksvagen", "Ferrari", "Bugatti", "Lamborghini", "Audi"]
lóerők = [i for i in range(200, 1500, 50)] # [200, 250, 300, 350, ..., 1400, 1450]


with open("2. félév/10ora/autok.csv", "w", encoding="utf-8") as f:
    for i in range(150):
        f.write(f"{random_rendszám()};{random.choice(márkák)};{random.choice(lóerők)}\n")