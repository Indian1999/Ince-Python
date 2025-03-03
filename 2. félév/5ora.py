import random
import math
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
összeg = 0
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        összeg += mtx[i][j]
print("Összeg:", összeg)
# 2. feladat: Határozzuk meg, hogy melyik elem a legkisebb a mátrixban:
minimum = mtx[0][0]
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        if mtx[i][j] < minimum:
            minimum = mtx[i][j]
print("Legkisebb elem:", minimum)
# 3. feladat: Határozzuk meg, hogy melyik elem a legnagyobb a mátrixban:
maximum = mtx[0][0]
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        if mtx[i][j] > maximum:
            maximum = mtx[i][j]
print("Legnagyobb elem:", maximum)
# 4. feladat: Határozzuk meg, a mátrix elemeinek az átlagát
elemek_száma = len(mtx) * len(mtx[0])
átlag = összeg / elemek_száma
print("Az elemek átlaga:", round(átlag,2))
# 5. feladat: Módosítsuk a mátrix elemeit úgy, hogy a negatív számokból csináljunk pozitívat
# azaz, vegyük a számok abszolút értékét (pl.: -5 -> 5)
mtx = [[int(math.fabs(mtx[i][j])) for j in range(len(mtx[i]))] for i in range(len(mtx))]
for row in mtx:
    print(row)
    
mtx = [[[k for k in range(4)] for j in range(4)] for i in range(3)]
print(mtx)

összeg = 0
for i in range(len(mtx)):
    for j in range(len(mtx[0])):
        for k in range(len(mtx[0][0])):
            összeg += mtx[i][j][k]
print("A kocka elemeinek az összege:", összeg)

import numpy as np                  #pip install numpy
import matplotlib.pyplot as plt     #pip install matplotlib

axes = [5,5,5] # tengelyek
data = np.ones(axes) # data, az egy 5*5*5 mátrix, ami csupa 1-eseket tartalmaz (floatként)
colors = np.empty(axes + [3]) # 4 dimenziós mátrix (5*5*5*3), az értékeik azok nincsenek beállítva
# A memóriában lefoglaljuk a helyet a mátrixnak, de nem adunk semmilyen alap értéket
# Ez azt eredményezi, hogy a mátrix elemei, azok az értékek lesznek, amik eredetileg,
# azon a memória helyen fellelhetőek voltak
colors[0] = [1,0,0] # Piros
colors[1] = [0,1,0] # Zöld
colors[2] = [0,0,1] # Kék
colors[3] = [1,1,0] # Sárga
colors[4] = [0,1,1] # Türkiz

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.voxels(data, facecolors=colors, edgecolors="gray")
plt.savefig("3d_kocka.png")
plt.show()


