import random
lista = []
for i in range(20):
    lista.append(random.randint(-10, 10))
print(lista)
# 1. feladat: Számoljuk meg a páros, páratlan, pozitív, negatív és 0 számokat egy listában
paros_szamlalo = 0
paratlan_szamlalo = 0
poz_szamlalo = 0
neg_szamlalo = 0
nulla_szamlalo = 0
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        paros_szamlalo += 1
    else:
        paratlan_szamlalo += 1
    if lista[i] > 0:
        poz_szamlalo += 1
    elif lista[i] < 0:
        neg_szamlalo += 1
    else:
        nulla_szamlalo += 1
print(f"Párosak száma: {paros_szamlalo} db\nPáratlanok száma: {paratlan_szamlalo} db\nPozitívak: {poz_szamlalo} db\nNegatívak: {neg_szamlalo} db\nNullák: {nulla_szamlalo} db")

# 2. feladat: A legnagyobb különbség két szám között egy listában
minimum = min(lista)
maximum = max(lista)
print(f"A legkisebb szám: {minimum}, a legnagyobb szám: {maximum}, a kettő különbsége: {maximum-minimum}")

# 3. feladat: Töröljük a duplikációkat a listából
print(lista)
egyedi_lista = []
for i in range(len(lista)):
    if lista[i] not in egyedi_lista:
        egyedi_lista.append(lista[i])
lista = egyedi_lista[:]
print(lista)

# 4. feladat: Találjuk meg a második legnagyobb számot
seged_lista = lista[:]
seged_lista.remove(max(seged_lista))
masodik_legnagyobb = max(seged_lista)
print("A lista második legnagyobb eleme:", masodik_legnagyobb)

# 5. feladat: rendezzük a listát

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - i -1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
bubble_sort(lista)
print(lista)

# 6. feladat: Az extend függvény
lista1 = [1, 53, 32, 12, 12]
lista2 = ["asd", True, 11, "cica"]
lista1.extend(lista2)
print(lista1)

# 7. feladat: Szedjük ki az inteket egy listából
myList = [13, 15.02, "cica", [True, 12, "asd"], True, False, 99, 14, 3.14, "kutya"]
newList = []
for i in range(len(myList)):
    if type(myList[i]) == int:
        newList.append(myList[i])
print(newList)

# 8. feladat: Találjuk meg két lista közös elemeit
lista1 = []
for i in range(20):
    lista1.append(random.randint(-20, 20))
lista2 = [random.randint(-20, 20) for i in range(20)]
print(lista1)
print(lista2)

common_list = []
for item in lista1:
    if (item in lista2) and (item not in common_list):
        common_list.append(item)
print(common_list)

# 9. feladat: Egy lista elemeiből készítsünk 1 számot
# [4, 87, 12, 8] -> 487128
lista = [4, 87, 12, 8]
num_string = ""
for num in lista:
    num_string += str(num)
num = int(num_string)
print(num)
