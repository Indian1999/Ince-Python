class Vasarlas:
    def __init__(self, lista:list = []):
        self.termekek = lista.copy()

def beolvasas() -> list[Vasarlas]:
    with open("3. félév/penztar.txt", "r", encoding="utf-8") as f:
        vasarlasok = []
        aktualis_vasarlas = []
        for line in f:
            line = line.strip()
            if line != 'F':
                aktualis_vasarlas.append(line)
            else:
                vasarlasok.append(Vasarlas(aktualis_vasarlas))
                aktualis_vasarlas = []
        return vasarlasok
    
vasarlasok = beolvasas()

# 2. feladat:
print("2. feladat")
print("A fizetések száma:", len(vasarlasok))
print()

print("3. feladat")
print(f"Az első vásárló {len(vasarlasok[0].termekek)} darab árucikket vásárolt.")
print()

print("4. feladat")
sorszam = int(input("Adja meg a vásárlás sorszámát: ")) - 1
arucikk = input("Adja meg az árucikk nevét: ")
darabszam = int(input("Adja meg a vásárolt darabszámot: "))
print()

print("5. feladat")
szamlalo = 0
utolso_index = None
elso_index = None
for i in range(len(vasarlasok)):
    if arucikk in vasarlasok[i].termekek:
        szamlalo += 1
        utolso_index = i
        if szamlalo == 1:
            elso_index = i
print(f"Az első vásárlás sorszáma: {elso_index + 1}")
print(f"Az utolsó vásárlás sorszáma: {utolso_index + 1}")
print(f"{szamlalo} vásárlás során vettek belőle.")
print()

def ertek(db):
    if db == 1:
        return 500
    elif db == 2:
        return 950
    else:
        return 950 + 400 * (db - 2)
    
print("6. feladat")
print(f"{darabszam} darab vételekor fizetendő: {ertek(darabszam)}")
print()