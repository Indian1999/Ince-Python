class LottoHuzas:
    def __init__(self, év, hét, dátum, hatos_db, hatos_ft, ötös_db, ötös_ft, négyes_db, négyes_ft, hármas_db, hármas_ft, szám1, szám2, szám3, szám4, szám5, szám6):
        self.év = év
        self.hét = hét
        self.dátum = dátum
        self.hatos_db = hatos_db
        self.hatos_ft = hatos_ft
        self.ötös_db = ötös_db
        self.ötös_ft = ötös_ft
        self.négyes_db = négyes_db
        self.négyes_ft = négyes_ft
        self.hármas_db = hármas_db
        self.hármas_ft = hármas_ft
        self.szám1 = szám1
        self.szám2 = szám2
        self.szám3 = szám3
        self.szám4 = szám4
        self.szám5 = szám5
        self.szám6 = szám6
def beolvasás(fileName):
    huzasok = []
    f = open(fileName, "r", encoding="utf-8")
    for sor in f:
        sor = sor.strip() # Az üres karaktereket leszedi az elejéről és a végéről
        adatok = sor.split(";") # ["2023", "22", "2023.06.04", "0", "0Ft"; "33"; "392812Ft", ...]
        huzas = LottoHuzas(int(adatok[0]), int(adatok[1]), adatok[2],
                           int(adatok[3]), int(adatok[4][0:-2]),    #hatos találatok
                           int(adatok[5]), int(adatok[6][0:-2]),    #ötös találatok
                           int(adatok[7]), int(adatok[8][0:-2]),    #négyes találatok
                           int(adatok[9]), int(adatok[10][0:-2]),    #hármas találatok
                           int(adatok[11]), #szám1
                           int(adatok[12]), #szám2
                           int(adatok[13]), #szám3
                           int(adatok[14]), #szám4
                           int(adatok[15]), #szám5
                           int(adatok[16]) #szám6
                           )
        huzasok.append(huzas)
    f.close()
    return huzasok
def negyedik(huzasok):
    print("4.feladat:")
    print(f"\tA hatos.txt állomány {len(huzasok)} hét lottóhúzásainak az adatait tartalmazza.")
def ötödik(huzasok):
    számláló = 0
    for huzas in huzasok:
        if huzas.hatos_db > 0:
            számláló += 1
    százalék = számláló / len(huzasok) * 100
    print("5.feladat:")
    print(f"\tA lottóhúzások {round(százalék, 2)}%-nál volt 6-os találat.")
def ossznyeremeny(huzas):
    összeg = huzas.hatos_db * huzas.hatos_ft + huzas.ötös_db * huzas.ötös_ft + huzas.négyes_db * huzas.négyes_ft + huzas.hármas_db * huzas.hármas_ft
    return összeg
def hetedik(huzasok):
    összeg = 0
    for huzas in huzasok:
        összeg += ossznyeremeny(huzas)
    print("7.feladat:")
    print(f"\tEgy héten átlagosan {round(összeg/len(huzasok))} Ft-ot fizetett ki a lottó szervezője egy héten.")
def nyolcadik(huzasok):
    szamok_darab = [0 for i in range(46)] # 46 db 0-t rak a listába
    for huzas in huzasok:
        szamok_darab[huzas.szám1] += 1
        szamok_darab[huzas.szám2] += 1
        szamok_darab[huzas.szám3] += 1
        szamok_darab[huzas.szám4] += 1
        szamok_darab[huzas.szám5] += 1
        szamok_darab[huzas.szám6] += 1
    leggyakoribb_szamok = []
    for j in range(6):
        max_index = 0
        for i in range(len(szamok_darab)):
            if szamok_darab[i] > szamok_darab[max_index]:
                max_index = i
        leggyakoribb_szamok.append(max_index)
        szamok_darab[max_index] = -1
    print("8.feladat:")
    print("\tA hat leggyakrabban kihúzott szám:", leggyakoribb_szamok)
def kilencedik(huzasok):
    hatosok_évente = {} # üres dictionary létrehozása (szótár)
    for huzas in huzasok:
        if not huzas.év in hatosok_évente:
            hatosok_évente[huzas.év] = huzas.hatos_db
        else:
            hatosok_évente[huzas.év] += huzas.hatos_db
    print("9.feladat:")
    for key in hatosok_évente.keys():
        print(f"\t{key}: {hatosok_évente[key]}")
def ossz_nyertes_szelveny(huzas):
    return huzas.hatos_db + huzas.ötös_db + huzas.négyes_db + huzas.hármas_db
def tizedik(huzasok):
    f = open("nyertesSzelvenyek.txt", "w", encoding="utf-8")
    for huzas in huzasok:
        f.write(f"{huzas.dátum};{ossz_nyertes_szelveny(huzas)}\n")
    f.close()
    print("10.feladat:")
    print("\tA nyertesSzelvenyek.txt file sikeresen létrehozva.")

huzasok = beolvasás("hatos.txt")
negyedik(huzasok)
ötödik(huzasok)
hetedik(huzasok)
nyolcadik(huzasok)
kilencedik(huzasok)
tizedik(huzasok)
