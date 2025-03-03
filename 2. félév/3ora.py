from random import randint
from random import randrange
import math
import numpy as np # erre a modulra np-ként tudok hivatkozni
import matplotlib.pyplot as plt # pip install matplotlib.pyplot

print(randint(1, 10))
print(randrange(1,100))
print(math.e)
print(math.pi)
print(math.tau)

#r = float(input("Add meg egy kör sugarát!\n"))
r = 5
print("A kör kerülete (pi = 3.14):", 2*r*3.14)
print("A kör kerülete (pontos pi értékkel):", math.pi*2*r)

# Ceil függvény (ceiling) felfelé kerekít egy float értéket
print(math.ceil(3.14))  # felfelé kerekít
print(math.floor(3.14)) # lefelé kerekít

print(math.inf) # végtelen
print(math.nan) # not a number

lista = [1,2,3,4]
lista = np.array(lista)
print(lista) 
lista.resize(2,2)
print(lista) 
lista.resize(2,2,1)
print(lista)

random_számok = np.random.randint(0, 100, size = (5, 10))
print(random_számok)
print("Szórás:", random_számok.std())
print("Átlag:", random_számok.mean())
print("", random_számok.flatten()) # 1 dimenzióssá alakítja a mátrixot

lin_szamok = np.linspace(0, 100, num = 11)
print(lin_szamok)
lin_szamok2 = np.linspace(5, 200, 10)
print(lin_szamok2)

matrix1 = np.random.randint(0,2, size = (2,2))
print(matrix1)
matrix2 = np.random.randint(1, 10, size = (10,2))
print(matrix2)
print(np.dot(matrix2, matrix1))

def f(x):
    return 2*x + 3

def g(x):
    return x**2 + 3*x - 3

értelmezési_taromány = np.linspace(-5, 5, num = 501)
y_tengely = f(értelmezési_taromány)
g_függvény = g(értelmezési_taromány)

#plt.plot(értelmezési_taromány, y_tengely)
#plt.plot(értelmezési_taromány, g_függvény)
#plt.title("f(x) = 2x + 3   Vs.   g(x) = x^2 + 3x - 3")
#plt.xlabel("x tengely")
#plt.ylabel("y tengely")
#plt.grid(True)
#plt.show()

#plt.scatter(x=értelmezési_taromány, y=y_tengely)
#plt.show()

# Feladat: Van 20 robotunk, akik egy 20 * 20 -as táblán mozognak

tábla = np.random.randint(0,1, size=(20,20))
for i in range(5, 15):
    tábla[10, i] = 1
print(tábla)
    
def move_robots():
    for i in range(len(tábla)):
        for j in range(len(tábla[0])):
            irány = randint(1, 4)
            if irány == 1 and j != 0 and tábla[i][j] >= 1:
                tábla[i][j] -= 1
                tábla[i][j-1] += 1    
            if irány == 2 and j != len(tábla[0]) - 1 and tábla[i][j] >= 1:
                tábla[i][j] -= 1
                tábla[i][j+1] += 1    
            if irány == 3 and i != 0 and tábla[i][j] >= 1:
                tábla[i][j] -= 1
                tábla[i-1][j] += 1    
            if irány == 4 and i != len(tábla) - 1 and tábla[i][j] >= 1:
                tábla[i][j] -= 1
                tábla[i+1][j] += 1    
                
plt.imshow(tábla)
plt.savefig("3ora_kepek/robots0")
for i in range(1, 101):
    move_robots()
    plt.imshow(tábla)
    plt.savefig(f"3ora_kepek/robots{i}")