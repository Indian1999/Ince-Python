# 1. feladat: legyen a két lista ugyan olyan
list_1 = [43, 70, 25, 39, 15, 85, 42, 94, 11, 76, 20,  36, 48]
list_2 = [ 36, 44, 20, 96, 69, 15, 27, 14, 87, 67, 97, 43,  8, 22]

for item in list_2:
    if item not in list_1:
        list_1.append(item)

for item in list_1:
    if item not in list_2:
        list_2.append(item)

print(sorted(list_1)) 
print(sorted(list_2)) 


# 2. feladat: rendezett-e a lista? szigorú monoton növekvő-e?
lista = [43, 70, 25, 39, 15, 85, 42, 94, 11, 76, 20,  36, 48]
lista2 = [12, 14, 17, 20, 21, 21, 22, 22, 45, 47, 89, 99, 100]
lista3 = [14, 16, 17, 18, 19, 23, 25, 87, 92, 94, 98, 99, 100]
def is_sorted(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i+1]:
            return False
    return True

def is_stricktly_incresing(lista):
    for i in range(len(lista) - 1):
        if lista[i] >= lista[i+1]:
            return False
    return True

print("is_sorted():")
print(is_sorted(lista))
print(is_sorted(lista2))
print(is_sorted(lista3))
print("is_stricktly_increasing():")
print(is_stricktly_incresing(lista))
print(is_stricktly_incresing(lista2))
print(is_stricktly_incresing(lista3))

# 3. feladat: Írjuk ki az 1000-nél olcsóbb termékeket
items = ["apple", "book", "bread", "cheese", "chicken", "curry sauce", "doughnut", "toilet roll", "socks", "toothpaste"]
prices = [1500, 1000, 700, 1600, 1900, 600, 800, 999, 500, 550]
for i in range(len(prices)):
    if prices[i] < 1000:
        print(f"{items[i]} - {prices[i]} Ft")
# Írjuk ki a legolcsóbb terméket
min_index = 0
for i in range(len(prices)):
    if prices[min_index] > prices[i]:
        min_index = i
print(f"A legolcsóbb termék: {items[min_index]} - {prices[min_index]} Ft")

# Írjuk ki a legdrágább terméket

# Írjuk ki a termékek átlagos árát

# Írjuk ki azokat a termékeket amik drágábbak, mint 999 Ft, de olcsóbbak, mint 1600Ft

# 4. feladat: Határozzuk meg a 100. fibonacci számot
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
fib_lista = [1,1]
a = 1
b = 1
for i in range(150):
    c = a + b
    fib_lista.append(c)
    a = b
    b = c
print("A fibonacci sorozat 100. eleme:", fib_lista[99])

# 5. feladat: Futás eredmények, rendezzük a listákat
names = ["Bob", "Wanda", "Jared", "Emma", "Lisa", "Fred", "George", "Noah", "Rachel"]
times = [123.42, 67.15, 80.70, 118.40, 99.95, 68.22, 71.51, 102.68, 80.88]

for i in range(len(times)):
    for j in range(len(times)):
        if times[i] < times[j]:
            times[i], times[j] = times[j], times[i]
            names[i], names[j] = names[j], names[i]

print(names)
print(times)

# Írjuk ki a dobogósok neveit és az elért időeredményüket
print("Dobogósok:")
print(f"{names[0]} - {times[0]} mp")
print(f"{names[1]} - {times[1]} mp")
print(f"{names[2]} - {times[2]} mp")

# Írjuk ki az átlagos időt
print("Átlagos idő:", round(sum(times) / len(times), 2))

# Írjuk ki az utolsó helyezettet és az elért eredményét
print(f"Utolsó: {names[-1]} - {times[-1]} mp")

# Írjuk ki azokat az emebereket az eredményükkel együtt, akik 100 mp alatt teljesítették a távot

for i in range(len(times)):
    if times[i] < 100:
        print(f"{names[i]} - {times[i]} mp")



