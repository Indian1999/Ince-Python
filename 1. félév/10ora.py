#Print függvény kiegészítések
"""
num = 10
szöveg = "cica"
print(num)
print(szöveg)

#Több paraméterrel hívjuk meg a print függvényt
print("num =", num)
print("szöveg =", szöveg)
print(num, szöveg) #10 cica     Az argumentumokat alapból szóközzel választja el

#Ha több dolgot akarunk kiírni, azt is meg tudjuk tenni egy argumentummal
print("szöveg = " + szöveg) # 1 argumentumunk van, összeadtunk két stringet
print("num = " + str(num))

#A print függvény kulcsszavas paraméterei:
# sep - meghatározza, hogy milyen stringet helyezzen az argumentumok közé (alapból egy szókösz)
print(1,2,3,4,5) #1 2 3 4 5
print(1,2,3,4,5, sep=",") #1,2,3,4,5 Az argumentumokat ","-vel fogja elválasztani
print(1,2,3,4,5, sep=", ") #1, 2, 3, 4, 5 
print(1,2,3,4,5, sep="kiskutyka")  #1kiskutyka2kiskutyka3kiskutyka4kiskutyka5

# end - Meghatározza, hogy milyen stringet helyezzen a kiírás végére (alapból \n [enter])

for i in range(5):
    print(i, end=" ") #0 1 2 3 4

#Amire figyelni, hogy ilyenkor nem rak entert a végére, ezért ha újra kiírnánk valamit, azt
#ugyan abba a sorba fogja kiírni
print() # Ha üres a print, akkor csak egy entert ír ki
print("almafa")

# 1. feladat: Írjunk egy programot ami egy grammban megadott tömeget kg-ra vált
gramm = int(input("Add meg a tömeget grammban:\n"))
kg = gramm / 1000
print("Ez a mennyiég kg-ban: " + str(kg) + "kg")

# 2. feladat: Váltsunk Fahrenheit és Celsius között
# alt gr + 5 -> °    (kétszer kell megynomni)
fahrenheit = int(input("Add meg a Fahrenheit hőfokot:\n"))
celsius = (fahrenheit - 32) / 1.8
print(f"{fahrenheit} F° = {round(celsius, 2)} C°")

# 2. feladat b része: ugyan ez visszafelé

# 3. feladat: végzés időpontjának kiszámítása
időpont = input("Add meg e kezdés időponját (óó:pp [8:15])!\n") # "13:45"
időtartam = int(input("Add meg, hogy hány perc az időtartam!\n"))
időpont_külön = időpont.split(":") # ['8', '15']
óra = int(időpont_külön[0])
perc = int(időpont_külön[1])
időpont_perc = óra * 60 + perc
végzés_perc = időpont_perc + időtartam #1335
vége_óra = végzés_perc // 60 % 24
vége_perc = végzés_perc % 60
print(f"A végzés időpontja: {vége_óra}:{vége_perc}")
"""
# feladat: Collatz-sejtés
num = int(input("Add meg, hogy honnan indítsam a collatz sejtést!\n"))
collatz = [num]
while num != 1:
    if num % 2 == 0:
        num //= 2
    else:
        num = num * 3 + 1
    collatz.append(num)

print(collatz)
print(collatz[-1])

# feladat: milyen háromszög?
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

#1. lépés: létezik-e egyáltalán:
if a + b > c and a + c > b and b + c > a:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Derékszögű")
    if a == b and b == c:
        print("Szabályos")
    elif a == b or b == c or a == c:
        print("Egyenlő szárú")
else:
    print("Ilyen háromszög nem létezik!")

