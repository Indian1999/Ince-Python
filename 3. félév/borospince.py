# Link: https://richardkorom.hu/feladatok/programozas/oop/#

class BorospinceException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Bor:
    def __init__(self, evjarat, fajta, alkoholtartalom = 12.5):
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
        

bor1 = Bor(2000, "vörös")
bor1.setEvjarat(2015)
print(bor1.getEvjarat())
    