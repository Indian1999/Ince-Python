import random

#1.feladat
szam = float(input("Adj meg egy számot: "))

negyzet = szam ** 2

print("A szám négyzete:", negyzet)

#2.feladat
a = float(input("Add meg az első számot: "))
b = float(input("Add meg a második számot: "))
if a > b:
    print("A nagyobb szám:", a)
elif b > a:
    print("A nagyobb szám:", b)
else:
    print("A két szám egyenlő.")

#3.feladat
lista = [3, 4, 12, 7, 8, 15, 20, 21]

paros_db = 0
for szam in lista:
    if szam % 2 == 0:
        paros_db += 1

print("A listában található páros számok száma:", paros_db)

#4.feladat
for i in range(1, 11):
    print(i)

#5.feladat
xy = int(input("Adj meg egy számot: "))
i = 1
while i <= xy:
    print(i)
    i += 1

#6.feladat

def difference(a, b):
    diff = a - b
    if diff < 0:
        return -diff
    return diff

print(difference(7, 15))

#7.feladat
def poz_neg_nulla(x):
    if x > 0:
        return "pozitív"
    elif x < 0:
        return "negatív"
    else:
        return "nulla"

#8.feladat
szamok = [12, 5, 27, 9, 18]
legnagyobb = szamok[0]        

for szam in szamok:
    if szam > legnagyobb:
        legnagyobb = szam

print("A legnagyobb szám:", legnagyobb)

#9.feladat
szoveg = "almafa alatt áll a lány és almát eszik."

a_db = 0

for karakter in szoveg:
    if karakter == 'a':
        a_db += 1

print("Az 'a' betűk száma:", a_db)

#10.feladat
eredeti = [1, 2, 3, 4, 5]
forditott = []

for elem in eredeti:
    forditott.insert(0, elem)

print("Eredeti lista:", eredeti)
print("Megfordított lista:", forditott)

# 11. Hozz létre egy dictionary-t 3 kulccsal (név, kor, város), majd írd ki a kulcs–érték párokat.

user = {
    "name": "Kis Pista",
    "age": 36,
    "city": "Budapest"
}
# Ha a kulcsokon megyünk végig:
for key in user.keys():
    print(f"{key}: {user[key]}")

# Ha a kulcs-érték párokon megyünk végig

for key, value in user.items():
    print(f"{key}: {value}")



# 12. Írj programot, amely tuple-be ment 3 számot, majd kiírja a második elemet.
myTup = (4, 2, 7)
print(myTup[1])

#13.feladat
helyes_jelszo = "python123"
while True:
    jelszo = input("Kérlek, írd be a jelszót: ")
    if jelszo == helyes_jelszo:
        print("Helyes jelszó! Beléptél.")
        break  
    else:
        print("Helytelen jelszó, próbáld újra.")

#14.feladat
szam = int(input("Kérlek, adj meg egy számot: "))
if szam % 3 == 0 and szam % 5 == 0:
    print(f"A {szam} osztható 3-mal és 5-tel egyszerre.")
else:
    print(f"A {szam} nem osztható 3-mal és 5-tel egyszerre.")

#15.feladat
lista = [0, 1, 2, 0, 3, 0, 4, 5]
while 0 in lista:
    lista.remove(0)

print("A lista 0-k nélkül:", lista)

#16.feladat
def osszeg(lista):
    összeg = 0
    for item in lista:
        összeg += item
    return összeg
szamok = [1, 2, 3, 4, 5]
print("A lista elemeinek összege:", osszeg(szamok))

#17.feladat
sugar = float(input("Kérlek, add meg a kör sugarát: "))

pi = 3.14
terulet = pi * sugar ** 2

print(f"A kör területe: {terulet}")

#18.feladat
for szam in range(1, 21):
    if szam % 2 != 0:
        print(szam)

#19.feladat
lista = [random.randint(1, 15) for i in range(30)]
print(lista)
uj_lista = []
for item in lista:
    if item not in uj_lista:
        uj_lista.append(item)

print(uj_lista)

uj_lista = list(set(lista))
print(uj_lista)


#20.feladat
szam = random.randint(1, 10)

while True:
    tipp = int(input("Gondoltam egy számra 1 és 10 között. Mi a tipped? "))
    if tipp == szam:
        print("Gratulálok! Eltaláltad a számot!")
        break
    elif tipp > szam:
        print(f"Ettől kisebbre gondoltam")
    else:
        print("Ettől nagyobbra gondoltam")

"""
gyakorlni:
dictionary feladatok
tuple-t átismeteljük
"""
# 1. Írj programot, amely bekér egy számot a felhasználótól, és kiírja a szám négyzetét.
# 2. Kérj be két számot, és írd ki a nagyobbat. Ha egyenlők, jelezd.
# 3. Írj programot, amely megszámolja, hány páros szám van egy előre megadott listában.
# 4. Készíts programot, amely 1-től 10-ig kiírja a számokat egy for ciklussal.
# 5. Írj kódot, amely while ciklussal számolja 1-től addig a számig, amit a user megad.
# 6. Készíts egy függvényt, amely két számot vár, és visszaadja a különbségüket.
# 7. Írj függvényt, amely eldönti egy számról, hogy pozitív, negatív vagy nulla.
# 8. Hozz létre egy listát 5 tetszőleges számmal, és írd ki a lista legnagyobb értékét beépített függvény nélkül.
# 9. Írj programot, amely egy szövegben megszámolja az 'a' betűk számát.
# 10. Írj programot, amely egy lista elemeit megfordítja (reverse) új lista létrehozásával.
# 11. Hozz létre egy dictionary-t 3 kulccsal (név, kor, város), majd írd ki a kulcs–érték párokat.
# 12. Írj programot, amely tuple-be ment 3 számot, majd kiírja a második elemet.
# 13. Készíts programot, amely bekér egy jelszót, és addig kér újra, amíg a felhasználó a "python123" szót nem írja be.
# 14. Kérj be egy számot, és írd ki róla, hogy osztható-e 3-mal és 5-tel egyszerre.
# 15. Írj programot, amely egy listából eltávolít minden 0 értéket.
# 16. Hozz létre egy függvényt, amely egy listát vár, és visszaadja a lista elemeinek összegét.
# 17. Írj programot, amely bekéri egy kör sugarát, majd kiszámolja a kör területét (π = 3.14).
# 18. Készíts programot, amely 1-től 20-ig kiírja csak a páratlan számokat.
# 19. Írj programot, amely egy megadott lista duplikált elemeit kiszűri (új listába gyűjti az egyedi értékeket).
# 20. Hozz létre egy egyszerű számkitalálós játékot 1 és 10 között (a program választ számot, a user tippel).
