#Ciklusok (while, for)
#Listák
"""
for i in range(5): # [0,1,2,3,4]
    print(i, end=" ")
print("szia")
print("hello")

for i in range(5, 10): #[5,6,7,8,9]
    print(i, end=" ")
print()

for i in range(20, 10, -1): # [20, 19, 18, ..., 12, 11]
    print(i, end=" ")
print()

for i in range(5, 51, 5): # [5, 10, 15, 20, ..., 45, 50]
    print(i, end=" ")
print() 

num = int(input("Adj meg egy számot és én eldöntöm, hogy prím-e!\n"))
isPrime = True
for i in range(2, num):
    if num % i == 0:
        isPrime = False
if isPrime:
    print("Ez egy prím szám!")
else:
    print("Ez nem egy prím szám!")

lista = ["kutya", "cica", "elefánt", "majom", "egér"]
for i in lista:
    print(i)

#while ciklus (elől tesztelős ciklus)
while True: # mindig ciklus (folyamatosan ismétel) Végtelen ciklus
    szöveg = input()
    if szöveg == "quit":
        break # ha break-hez a programm, akkor kilép az aktuális ciklusból

num = 0
while num < 11:
    num += 1
    if num % 2 == 0:
        continue # ha ide ér a program, akkor az aktuális ciklus futást skippeli
    print(num)
"""
#Programozási tételek:

lista = [7,3,1,5,9,34,-6,0,-8,-9,4,-10,12,4,6,1,99,86,-78]
print(lista)

# Maximum kiválasztás
legnagyobb = lista[0]
for item in lista:
    if item > legnagyobb:
        legnagyobb = item
print("A legnagyobb szám:", legnagyobb)

# Minimum kiválasztás
legkisebb = lista[0]
for item in lista:
    if item < legkisebb:
        legkisebb = item
print("A legkisebb szám:", legkisebb)

# Lineáris keresés:
# Megkeresi, hogy benne van-e egy elem a listában, és ha igen, akkor hanyadik elem

num = int(input("Adj meg egy számot és megnézem, hogy hol van a listában!\n"))
index = -1
for i in range(len(lista)):
    if lista[i] == num:
        index = i
        break
print(num, "a", index, ". indexen található!")

# Eldöntés tétele:
# Eldönti, hogy egy bizonyos feltétel, igaz- e a listára

#Döntsük el, hogy van-e negatív szám a listában

vanNegativ = False
for item in lista:
    if item < 0:
        vanNegativ = True
        break

if vanNegativ:
    print("Van a listában negatív szám!")
else:
    print("Nincs a listában negatív szám!")

#Összegzés tétele:
#Összeadja a lista elemeit

összeg = 0
for item in lista:
    összeg += item
print("A lista elemeinek az összege:", összeg)
print("A lista elemeinek az átlaga:", összeg/len(lista))

#Szétválogatás tétele:
# Két vagy több új listába szétszortírozza az eredeti listát

# Szortírozzunk pozitív és negatív értékek szerint

pozLista = []
negLista = []
for item in lista:
    if item > 0:
        pozLista.append(item)
    if item < 0:
        negLista.append(item)

print(pozLista)
print(negLista)

# Feltételes összegzés
# A pozitív számokat adjuk össze a listában

summa = 0
for item in lista:
    if item > 0:
        summa += item

print("A pozitív számok összege:", summa)

# Adjuk össze a 3-mal osztható számokat

summa = 0
for item in lista:
    if item % 3 == 0:
        summa += item

print("A 3-mal osztható számok összege:", summa)