#Mai óra tartalma:
#aritmetikai operátorok (+, -, *, /, %, //, **)

print(4 + 9) # 13
print(9 - 4) # 5
print(9 * 4) # 36
print(9 / 4) # 2.25 Az osztás eredménye mindig float
print(9 % 4) # 1    Megadja az osztási maradékot
print(9 // 4)# 2    Megnézi hány egészszer van meg benne a szám
print(2 ** 10) #2^10 = 1024  hatványozás
print(8 // 2)# 4
print(8 / 2) # 4.0

#értékadó operátorok (=, +=, -=, *=, /=, %=, //=, **=)

print("Értékadó operátorok:")
num = 5
print(num) #5
num += 8
print(num) #13
num -= 4
print(num) #9
num *= 3
print(num) #27
num /= 9
print(num) #3.0
num %= 2
print(num) #1.0
num += 50
print(num) #51.0
num //= 10
print(num) #5.0
num **= 4
print(num) #625.0

#összehasonlító operátorok (>, <, >=, <=, ==, !=)

if 5 > 2:
    print("5 > 2")
if 8 == 8:
    print("8 = 8")
if 8 != 7:
    print("8 != 7")

#logikai operátorok (and, or, not)
barana_haju = True
kek_szemu = False

if (barana_haju and kek_szemu):
    print("nem fog lefutni, mert az egyik hamis")

if (barana_haju or kek_szemu):
    print("Elég ha az egyik igaz")

if (not kek_szemu):
    print("Ha nem kék szemű az illető")

#in operator - megnézi, hogy egy elem benne van-e a listában
lista = [4, 8, 7, 9, 3, 1]

if 4 in lista:
    print("Lefut ha a 4 benne van a listában")

if 1 in lista:
    print("Akkor futna le, ha az 1 benne lenne a listában")


#1. feladat: Írjuk ki az első 10 pozitív egész számot, és adjuk meg ezek összegét!
#b, határozzuk meg az első 10 szám szorzatát

print("Az első 10 pozitív egész szám:")
összeg = 0
szorzat = 1
for i in range(1, 11, 1):
    print(i)
    összeg += i
    szorzat *= i
print("Az összegük:", összeg)
print("A szorzatuk:", szorzat)
# szorzat = 3 628 800

#2. feladat: Határozzuk meg egy számról, hogy hány számjegyből áll

num = 43287659284 #11
print(num)
számláló = 0
while num > 0:
    num //= 10
    számláló += 1
print("Ennyi számjegyből áll:", számláló)


#3. feladat: Írjuk ki a prímszámokat 1-től 100-ig

for i in range(2, 101):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
    if is_prime:
        print(i)

#4. feladat: Kérjünk be egy számot és írjuk ki annak a számnak a szorzótábláját (1-től 10-ig)!
#num = int(input("Adj meg egy számot!\n"))
for i in range(1,11):
    print(str(i) + " * " + str(num) + " = " + str(num*i))

#5. feladat: Kérjünk be egy hónapot (szám formában) és határozzuk meg, hogy melyik évszakban van!
#honap = int(input("Add meg egy hónap soszámát!\n"))

honap = 0
if honap == 12 or honap == 1 or honap == 2:
    print("Tél")
if honap == 3 or honap == 4 or honap == 5:
    print("Tavasz")
if honap >= 6 and honap <= 8:
    print("Nyár")
if honap == 9 or honap == 10 or honap == 11:
    print("Ősz")

#6. feladat: Kérjük be egy derékszögű háromszög 2 befogóját és mondjuk meg az átfogóját!

a = int(input("Add meg az első befogót:\n"))
b = int(input("Add meg a második befogót:\n"))
atfogo_negyzet = a ** 2 + b ** 2
atfogo = atfogo_negyzet ** 0.5
print("Átfogó:", atfogo)