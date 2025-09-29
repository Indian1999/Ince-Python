# Link: https://richardkorom.hu/feladatok/programozas/oop/#

class BorospinceException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Bor:
    def __init__(self, evjarat, fajta, alkoholtartalom = 12.5):
        if 0 > alkoholtartalom or 100 < alkoholtartalom:
            raise BorospinceException("Az alkoholtartalomnak 0 és 100 között kell lennie!")
        self.evjarat = evjarat
        self.fajta = fajta
        self.alkoholtartalom = alkoholtartalom

    def getEvjarat(self):
        return self.evjarat
    
    def setEvjarat(self, ev):
        self.evjarat = ev

    def getFajta(self):
        return self.fajta
    
    def setFajta(self, fajta):
        self.fajta = fajta

    def setAlkohol(self, alkohol):
        if 0 > alkohol or 100 < alkohol:
            raise BorospinceException("Az alkoholtartalomnak 0 és 100 között kell lennie!")
        self.alkoholtartalom = alkohol

    def __eq__(self, value):
        if type(value) != Bor:
            return False
        if self.evjarat == value.evjarat and self.fajta.lower() == value.fajta.lower() and self.alkoholtartalom == value.alkoholtartalom:
            return True
        return False
        
class Szekreny:
    def __init__(self):
        self.borok = []

    def get_bor(self, n: int) -> Bor:
        if type(n) != int:
            raise BorospinceException("Az index nem egész szám!")
        if n < 0 or n >= len(self.borok):
            raise BorospinceException("Nem létező index!")
        return self.borok[n]

    def __iadd__(self, value):
        if type(value) != Bor:
            raise TypeError("Nem bor!")
        self.borok.append(value)
        return self

bor1 = Bor(2000, "vörös")
bor2 = Bor(2023, "Villányi", 15)

polc = Szekreny()
polc += bor1
polc += bor2
print(polc.get_bor(0))