#Alapértelmezett paraméter értékek függvényekben (default value)

# Ha a függvény hívásakor nem adjuk meg a "növekvő" paramétert, akkor
# alapértelmezetten True értéke lesz
def rendezve(lista, növekvő = True):
    for i in range(len(lista) - 1):
        for j in range(i+1, len(lista)):
            if növekvő:
                if lista[i] > lista[j]:
                    lista[i], lista[j] = lista[j], lista[i] # Megcseréljük a két elemet
            else:
                if lista[i] < lista[j]:
                    lista[i], lista[j] = lista[j], lista[i] # Megcseréljük a két elemet
    return lista

lista = [4, 8, 3, 1, 33, 12, 4, 21, 24, 1, 7, 2, 12, 17, 20, 1, 0]
print(lista)
print(rendezve(lista))
print(rendezve(lista, True))
print(rendezve(lista, False))

#Rekurzív függvények
# Egy olyan függvény ami önmagát hívja meg
# faktoriális: 5! = 5 * 4 * 3 * 2 * 1 
# n! = n * (n-1)!
# 1! = 1
# 0! = 1
# fakt(n) = n * fakt(n-1)

def fakt(n):
    if n == 1 or n == 0:
        return 1
    return n * fakt(n - 1)

print(fakt(5))
print(fakt(10))

# Fontos szabályok a rekurzív függvényekhez:
# Mindig legyen arra lehetősége a függvénynek, hogy már ne hívja meg önmagát (n = 0 vagy 1) [degenerált eset]
# Győződjünk meg arról, hogy ezt a degenerált esetet el tudja érni a függvény

# Legyen az a(n) számtani sorozat
#a1 = -8
#a(n) = a(n-1) + 5      (d = 5)

def a(n):
    if n == 1:
        return -8
    return 5 + a(n-1)

print(a(5))
print(a(53))

# Legyen b(n) rekurzív sorozat
# b(1) = 1
# b(2) = 2
# b(n) = 3 * b(n-1) - 6 * b(n-2)

def b(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return 3 * b(n-1) - 6 * (n-2)

#lista = [b(i) for i in range(1, 31)]
print(lista)

#Fibonacci sorozat
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# fib(n) = fib(n-1) + fib(n-2)
# fib(1) = 1
# fib(2) = 1

from functools import cache
import sys
sys.setrecursionlimit(5000)

@cache
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(50)) # minimum 18000 év kiszámolni a számítógépnek
# Memóriát (cache) használva, egy másodperc tört része alatt eredményt kapunk
print(fib(1500)) #Maximum recursion depth reached

