import random
# 1. feladat: Olvassunk be 2 számot, majd írjuk ki azok szorzatát
#num1 = float(input("Add meg az első számot: "))
#num2 = float(input("Add meg a második számot: "))
#print(f"{num1} * {num2} = {round(num1 * num2, 8)}")

# 2. feladat: Progtételek
lista = [random.randint(-10, 10) for i in range(20)]
print(lista)

# Hány negatív szám van a listában?
számláló = 0
for item in lista:
    if item < 0:
        számláló += 1
print(f"A lista {számláló} negatív számot tartalmaz")

# Írjuk ki a számok átlagát

# Mennyi a páros számok összege?

# Írjuk át a negatív számokat a listában a -10 szeresükre ( -5 -> 50, -3 -> 30 stb...)
for i in range(len(lista)):
    if lista[i] < 0:
        lista[i] = -10 * lista[i]
print(lista)

# Írjunk egy függvényt ami megkap 2 számot és összemossa őket 1 számmá (123, 455 -> 123456)

def merge_integers(num1, num2):
    return int(str(num1) + str(num2))

print(merge_integers(432, 867))
print(merge_integers(1, 634))

# Írjunk egy függvényt ami kap egy egész számot (n) illetve egy másik értéket (value) (típus mindegy)
# és visszaad egy n elemű listát, ami n db value-t tartalmaz

def generate_list(n, value):
    lista = []
    for i in range(n):
        lista.append(value)
    return lista

print(generate_list(10, 0))
print(generate_list(5, "cica"))
print(generate_list(8, True))
print(generate_list(3, [1,2,3]))

# Írjunk egy függvényt ami megkap egy listát, és visszaadja a listában található legnagyobb értéket!

# Írjunk egy függvényt ami megkap egy nevet és kiírja, hogy "Hello <név>!" (nem ad vissza semmit)

# Írjunk egy függvényt ami megkap egy egész számot és egy logikai értéket, 
# ha logikai igaz, akkor visszaadja a szám tízszeresét,
# ha hamis, akkor visszaadja a szám felét



# DICTIONARY    kulcsokhoz értéket rendel

my_dict = {
    "kutya": "Buksi",
    "cica": "Cirmi",
    "nagyi": "Teréz",
    "apa": "Attila",
    "anya": "Katalin",
    "gyerek": "Attila"
}

print(my_dict["gyerek"]) # Attila

# Az item itt a my_dict kulcsain megy végig
for item in my_dict:
    print(item, end = " ")
print()

for item in my_dict.keys():
    print(f"{item} -> {my_dict[item]}")
print()

# Végigmehetünk csak az értékeken is
for item in my_dict.values():
    print(item, end= " ")
print()

# Egyszerre mindkettő
for item in my_dict.items():
    print(item)
    
for key, value in my_dict.items():
    print(key, value)
    



# Folyamatosan olvassunk be egy terméket a felhasználótól és rakjuk bele a kosarunkba
# Ha még nincs a kosárban ilyen termék, akkor 1 lesz benne,
# ha már van akkor csak 1-el növeljük

basket = {}

product = input("Rakj valamit a kosaradba: ")
while product != "":
    if product not in basket.keys():
        basket[product] = 1
    else:
        basket[product] += 1
    print(basket)
    product = input("Rakj valamit a kosaradba: ")
    