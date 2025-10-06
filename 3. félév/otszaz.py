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
