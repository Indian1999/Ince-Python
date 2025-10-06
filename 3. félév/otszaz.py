class Vasarlas:
    def __init__(self, lista:list = []):
        self.termekek = lista

def beolvasas() -> list[Vasarlas]:
    with open("3. félév/penztar.txt", "r", encoding="utf-8") as f:
        vasarlasok = []
        aktualis_vasarlas = Vasarlas()
        for line in f:
            line = line.strip()
            if line != 'F':
                aktualis_vasarlas.termekek.append(line)
            else:
                vasarlasok.append(aktualis_vasarlas)
                aktualis_vasarlas = Vasarlas()
        return vasarlasok
    
vasarlasok = beolvasas()

# 2. feladat:
print("2. feladat")
print("A fizetések száma:", len(vasarlasok))

