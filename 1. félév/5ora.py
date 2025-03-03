#Mai órán:
#python sajátosságia a listákat nézve

#        0. 1. 2. 3. 4. 
lista = [5, 8, 3, 9, 8]
print(lista[3]) #9

for item in lista: # item = 5, 8, 3, 9, 8
    print(item)

for i in range(len(lista)): # [0, 1, 2, 3, 4] i = 0, 1, 2, 3, 4
    print(lista[i])

#Negatív indexelés:

#       -5 -4 -3 -2 -1 
lista = [5, 8, 3, 9, 8]
print(lista[-1]) # a lista végéről az első elemet írja ki
print(lista[len(lista) -  1])

szöveg = "almafa" # string - karakterek lista
for char in szöveg:
    print(char)

print(szöveg[1])

# feladat - készítsünk egy programot amely mégnizi, hogy egy szöveg palindróm-e
# mindegy hogy milyen irányból olvassuk (görög)
# 5 betűs szó esetén 5//2  + 1 = 2 + 1 = 3
    # i = 0, 1, 2
# 6 betűs szó 6 // 2 = 3 (asddsa)
    #i = 0, 1, 2

# 0 1 2 3 4
#-5-4-3-2-1
# G Ö R Ö G

szöveg = 'input("Adj meg egy szöveget és én eldöntöm, hogy palindróm-e:\n")'
limit = 0
if len(szöveg) % 2 == 0:
    limit = len(szöveg) // 2
else:
    limit = len(szöveg) // 2 + 1

is_palindrome = True
for i in range(limit):
    if szöveg[i] != szöveg[-i - 1]:
        is_palindrome = False

if (is_palindrome):
    print("Ez a szöveg egy palindróm")
else:
    print("Ez nem egy palindróm")

# feladat: Add össze a pozitív számokat a listában és írd ki az eredményt
lista = [5, 8, -3, 7, -2, 4]
összeg = 0
for item in lista:
    if item > 0:
        összeg += item
print(összeg)

#pythonban lehet olyat csinálni, hogy a listának egy tartományát válasszuk ki
lista = [6,3,2,6,4,2,3,3,4,3,4]
print(lista)
print(lista[3:8]) # a 3. elemtől a 8-ig írjuk ki a számokat (a 8. már nicns benne) [6, 4, 2, 3, 3]
print(lista[3:-2]) # [6, 4, 2, 3, 3, 4]
print(lista[:7]) # Ha nem írok semmit a : elé, akkor az olyan mintha 0-t írtam volna [6, 3, 2, 6, 4, 2, 3]
print(lista[2:]) #A végéig fog menni [2, 6, 4, 2, 3, 3, 4, 3, 4]
print(lista[:]) # Egy az egyben visszaadja a listát [6, 3, 2, 6, 4, 2, 3, 3, 4, 3, 4]

lista = []
for i in range(1, 101):
    lista.append(i)
print(lista)

for i in range(len(lista) // 10):
    print(lista[ 0 + i * 10 : 10 + i * 10])

# feladat: Írj egy programot ami beolvas egy szöveget, és azt kiírja visszafelé

szöveg = "narancs"
uj_szöveg = ""
for i in range(len(szöveg)): # i = 0, 1, 2, 3, 4, 5, 6
    uj_szöveg += szöveg[-i - 1]
print(uj_szöveg)

szöveg = "a cica és az almafa"
print(szöveg.capitalize()) # A string első betűjét nagybetűssé teszi
print(szöveg.title()) # Minden szó első betűjét nagybetűssé teszi
print(szöveg.upper()) # Minden betű nagybetűs lesz
print(szöveg.lower()) # Minden betű kisbetűs lesz
print(szöveg.find("az")) #Megnézi, hogy a zárójelben található érték, hanyadik indexen van
print(szöveg.split(" ")) # Szóközek mentén, feldarabolja a szöveget, és visszaad egy listát

# feladat: Olvassunk be 3 számot (Háromszög oldalainak a hossza) és döntsük el, hogy létezik-e a háromszög



#List comprehension:

lista = [ 0 for i in range(5) ] # 5 alkalommal ismételd azt, hogy beleraksz egy 0-t a listába
#[0,0,0,0,0]
print(lista)
lista = [5 for i in range(6)]
print(lista) #[5,5,5,5,5,5]
lista = ["cica" for i in range(3)]
print(lista) # ['cica', 'cica', 'cica']

lista = [i for i in range(10)]
print(lista) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista = [i**2 for i in range(10)]
print(lista) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

import random # random könyvár betöltése

num = random.randrange(0, 10) # legkisebb: 0 legnagyobb: 9
print(num)