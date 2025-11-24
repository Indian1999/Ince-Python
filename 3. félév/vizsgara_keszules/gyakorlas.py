import random
random.seed(42)
# 1. Készíts egy listát az első 20 négyzetszámmal list comprehensionnel.

lista = [i**2 for i in range(1, 21)]
print(lista)

# 2. Szűrd ki egy 1-100 közötti lista elemei közül azokat, amelyek oszthatók 3-mal.
lista = [random.randint(1, 100) for i in range(50)]
print(lista)
oszthato_3_mal = [item for item in lista if item % 3 == 0]
print(oszthato_3_mal)

# 3. Írj függvényt, amely két számot kap és visszaadja az első számot második hatványon + a második szám.

def myFunction(a, b):
    return a**2 + b

print(myFunction(5, 3)) # 25 + 3 = 28
print(myFunction(10, 56)) # 156
print(myFunction(20, 577)) # 977

# 4. Írj függvényt, amely egy lista összegét adja vissza beépített sum nélkül.

def listSum(lista):
    total = 0
    for item in lista:
        total += item
    return total

print(listSum(lista))
print("Beépített függvény szerint:", sum(lista))

# 5. Írj rekurzív függvényt, amely kiszámítja n faktoriálisát.

def fakt(n):
    if n == 0:
        return 1
    return n * fakt(n-1)

print(fakt(5))

# 6. Írj rekurzív függvényt, amely megszámolja, hány szám van egy listában.
lista = [5, "asd", True, [5,6,3], 7.34, 99, False, "cica", 9, (4, 5, 3), 3.14, 8, 1, "kutya", 0.1]
def countNums(lista):
    if len(lista) == 0:
        return 0
    if type(lista[0]) == int or type(lista[0]) == float:
        return 1 + countNums(lista[1:])
    return countNums(lista[1:])

print(countNums(lista))

# 7. Írd ki a 10-től 0-ig visszaszámlálást range segítségével.

for i in range(10, -1, -1):
    print(i, end = " ")
print()

# 8. Készíts függvényt, amely két listát összefűz egy új listába, a + operátor használata nélkül.

def mergeLists(lista1, lista2):
    new_list = lista1[:]
    for item in lista2:
        new_list.append(item)
    return new_list

print(mergeLists([1,2,3], [4,5,6])) # [1, 2, 3, 4, 5, 6]

# 9. Készíts listát, amely egy adott szöveg összes karakterének ASCII kódját tartalmazza.
def get_ascii_list(string):
    ascii_list = []
    for char in string:
        ascii_list.append(ord(char))
    return ascii_list

print("A cica felmászott a fára.")
print(get_ascii_list("A cica felmászott a fára."))

# 10. Adj meg egy listát 1-20-ig, majd list comprehensionmel készíts új listát, 
# amelyben minden szám négyzete szerepel, de csak a páros számoké.
lista = [i for i in range(1, 21)]
new_list = [item**2 for item in lista if item % 2 == 0]
print(new_list) 

# 11. Írj egy függvényt ami egy lista átlagát számolja ki
jegyek = [3,2,5,4,1,5,4,5,3,2]
print("osztályzatok:", jegyek)
print("osztályzatok rendezve:", sorted(jegyek))

def atlag(lista):
    total = 0
    for item in lista:
        total += item
    if len(lista) == 0:
        return None
    return total / len(lista)

print("átlag:", atlag(jegyek))
# 12. Írj egy függvényt ami egy lista móduszát számolja ki
def modusz(lista):
    itemCounter = {}
    for item in lista:
        if item in itemCounter.keys():
            itemCounter[item] += 1
        else:
            itemCounter[item] = 1

    maxValue = -float("inf")
    maxKey = None
    for key, item in itemCounter.items():
        if item > maxValue:
            maxValue = item
            maxKey = key
    return maxKey

print("módusz:", modusz(jegyek))

# 13. Írj egy függvényt ami egy lista mediánját számolja ki

def median(lista):
    sorted_list = sorted(lista)
    if len(lista) % 2 == 0:
        midPoint = len(lista) // 2
        return (sorted_list[midPoint] + sorted_list[midPoint-1]) / 2
    else:
        midPoint = len(lista) // 2
        return sorted_list[midPoint]

print("medián:", median(jegyek))
# 14. Írj egy függvényt ami egy lista szórását számolja ki

def szoras(lista):
    if len(lista) == 0:
        return None
    average = atlag(lista)
    összeg = 0
    for item in lista:
        összeg += (item - average)**2
    return (összeg / len(lista)) ** 0.5 # feledik hatvány = négyzetgyök

print("szórás:", szoras(jegyek))

