import random

# Mátrixok (táblázat)
# Olyan listák amik listákat tárolnak

mtx = [
    [1,3,0,0,0,2,0,0,0],
    [0,0,1,3,0,0,1,3,0],
    [0,0,2,0,2,0,0,0,0],
    [0,0,1,3,0,0,0,0,0],
    [0,0,2,0,0,0,0,1,3],
    [0,0,6,0,0,0,1,3,0],
    [0,0,0,0,0,0,1,3,0],
    [0,0,0,1,3,0,0,1,3],
    [0,0,0,0,0,1,3,0,0]
]
for row in mtx:
    print(row)
    
print(mtx[5][2])

# Sor-oszlop bejárást kell végeznünk
# Programozási tételek mátrixokra:
összeg = 0
for i in range(len(mtx)): # végigmegyünk a sorokon
    for j in range(len(mtx[i])): # A soron belül végigmegyünk az elemeken
        összeg += mtx[i][j]
print("A mátrix elemeinek az összege:", összeg)

# List comprehension:
lista = [i for i in range(10, 20)] # [10, 11, 12, ..., 18, 19]
print(lista)
lista = [i**2 + 3*i for i in range(-5, 6)]
print(lista)
lista = [random.randint(0, 10) for i in range(10)]
print(lista)
lista = [[] for i in range(10)]
print(lista)
mtx = [[random.randint(-50, 100) for j in range(10)] for i in range(10)]
print("A mátrix tartalma:")
for row in mtx:
    print(row)
    
# 1. feladat: Határozzuk meg a mátrix elemeinek az összegét:

# 2. feladat: Határozzuk meg, hogy melyik elem a legkisebb a mátrixban:

# 3. feladat: Határozzuk meg, hogy melyik elem a legnagyobb a mátrixban:

# 4. feladat: Határozzuk meg, a mátrix elemeinek az átlagát

# 5. feladat: Módosítsuk a mátrix elemeit úgy, hogy a negatív számokból csináljunk pozitívat
# azaz, vegyük a számok abszolút értékét (pl.: -5 -> 5)

