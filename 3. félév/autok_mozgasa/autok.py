import os

class Auto:
    def __init__(self, rendszam, ora, perc, sebesseg):
        self.rendszam = rendszam
        self.ora = int(ora)
        self.perc = int(perc)
        self.sebesseg = int(sebesseg)

#1.feladat
f = open(os.path.join(os.path.dirname(__file__),"jeladas.txt"), "r", encoding="utf-8")
autok = []
for sor in f:
    adat = sor.strip().split()
    if len(adat) == 4:
        a = Auto(adat[0], adat[1], adat[2], adat[3])
        autok.append(a)
f.close()
print("1. feladat: Adatok beolvasva.\n")

#2.fekadat
utolso = autok[-1]
print("2. feladat:")
print("Az utolso jeladas ideje:", utolso.ora, ":", utolso.perc)
print("Rendszama:", utolso.rendszam)
print()

#3.feladat
elso_rendszam = autok[0].rendszam
print("Elso auto:", elso_rendszam)
print("Jeladasok idopontjai:", end=" ")
for a in autok:
    if a.rendszam == elso_rendszam:
        print(str(a.ora) + ":" + str(a.perc), end=" ")
print("\n")

#4.feladat
print("4. feladat:")
ora = int(input("Ora: "))
perc = int(input("Perc: "))
db = 0
for a in autok:
    if a.ora == ora and a.perc == perc:
        db += 1
print("Jeladasok szama ebben az idopontban:", db)
print()

#5.feladat
print("5. feladat:")
max_seb = 0
for a in autok:
    if a.sebesseg > max_seb:
        max_seb = a.sebesseg
print("Legnagyobb sebesseg:", max_seb)
print("Ezen a sebessegen halado autok:")
for a in autok:
    if a.sebesseg == max_seb:
        print(a.rendszam, end=" ")

#6.feladat

rendszam = input("Kérlek add meg a rendszámot: ")
last_time = None
last_speed = None
total_km = 0.0
for auto in autok:
    if auto.rendszam == rendszam:
        if last_time == None:
            last_time = auto.ora * 60 + auto.perc
            last_speed = auto.sebesseg
            print(f"{auto.ora}:{auto.perc} {0.0} km")
        else:
            current_time = auto.ora * 60 + auto.perc
            elapsed_time = current_time - last_time
            distance_traveled = (elapsed_time / 60) * last_speed
            total_km += distance_traveled
            last_time = current_time
            last_speed = auto.sebesseg
            print(f"{auto.ora}:{auto.perc} {round(total_km ,1)} km")
