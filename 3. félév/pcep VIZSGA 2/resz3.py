# 8. feladat:
lista = [1,2,3]

bemenet = None
while bemenet != 0:
    #bemenet = int(input("Adj meg egy számot (vége = 0): "))
    bemenet = 0
    if bemenet != 0:
        lista.append(bemenet)

print(f"Lista: {lista}")
print(f"Elemek száma: {len(lista)}")
print(f"Összeg: {sum(lista)}")
print(f"Átlag: {round(sum(lista)/len(lista), 2)}")
print(f"Legnagyobb: {max(lista)}")
print(f"Legkisebb: {min(lista)}")
print(f"Növekvő sorrend: {sorted(lista)}")

# 9. feladat: mátrix
"""
print()

sor1 = input("1. sor: ")  # "1 2 3" -> [1, 2, 3]
sor2 = input("2. sor: ")
sor3 = input("3. sor: ")

sor1 = sor1.strip().split(" ") # ['1', '2', '3'] -> [1, 2, 3]
sor1 = [int(item) for item in sor1]

sor2 = sor2.strip().split(" ") # ['1', '2', '3'] -> [1, 2, 3]
sor2 = [int(item) for item in sor2]

sor3 = sor3.strip().split(" ") # ['1', '2', '3'] -> [1, 2, 3]
sor3 = [int(item) for item in sor3]

matrix = [sor1, sor2, sor3]

print("\nMátrix:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()"""

# 10. feladat:
nevek = ("Anna", "Béla", "Cecil", "Dénes", "Elemér")
jegyek = [3,5,2,1,3]

for i in range(len(nevek)):
    print(f"{nevek[i]}: {jegyek[i]}")

try:
    nevek[2] = "Csilla"
except Exception as ex:
    print(f"A tuple nem modosithato! ({ex.__class__})")

minindex = 0
for i in range(1, len(jegyek)):
    if jegyek[i] < jegyek[minindex]:
        minindex = i
jegyek[minindex] = 5
print("Új jegyek:", jegyek)
