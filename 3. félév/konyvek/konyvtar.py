import os

class Konyv:
    def __init__(self, cim, szerzo, kiadas_eve, oldalszam):
        self.cim = cim
        self.szerzo = szerzo
        self.kiadas_eve = kiadas_eve
        self.oldalszam = oldalszam
    
    def hosszu(self): # (4. feladat)
        if self.oldalszam > 300:
            return "hosszú"
        return "rövid"

konyvek = []
path = os.path.dirname(__file__) # konyvek mappa

with open(os.path.join(path, "konyvek-adatok.txt"), "r", encoding="utf-8") as f:
    sorok = f.readlines()
    for sor in sorok[1:]: # A mező sort kihagyjuk ('Egri csillagok;Gárdonyi Géza;1901;420\n')
        sor = sor.strip().split(";") # ['Egri csillagok', 'Gárdonyi Géza', '1901', '420']
        konyv = Konyv(sor[0], sor[1], int(sor[2]), int(sor[3]))
        konyvek.append(konyv)

# 1. feladat: könyvek átlagos oldalszáma

összeg = 0
for konyv in konyvek:
    összeg += konyv.oldalszam
atlag = összeg / len(konyvek)
print(f"A könyvek átlagos oldalszáma: {round(atlag, 2)}") # 342.5

# 2. feladat: Legrégebbi könyv címe és szerzője
min_index = 0
for i in range(1, len(konyvek)):
    if konyvek[i].kiadas_eve < konyvek[min_index].kiadas_eve:
        min_index = i
legregebbi = konyvek[min_index]
print(f"A legrégebbi könyv: {legregebbi.cim}, {legregebbi.szerzo}")

# 3. feladat: Megjelent könyvek száma adott évszám után

evszam = int(input("Adj meg egy évszámot: "))
szamlalo = 0
for konyv in konyvek:
    if konyv.kiadas_eve >= evszam:
        szamlalo += 1

print(f"{evszam} vagy az után megjelent könyvek száma: {szamlalo}")

# 5. feladat: Régi könyvek fájlba

with open(os.path.join(path, "regi-konyvek.txt"),"w", encoding="utf-8") as f:
    for konyv in konyvek:
        if konyv.kiadas_eve < 2000:
            f.write(f"{konyv.cim} ({konyv.hosszu()})\n")

