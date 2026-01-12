szamok = [23, 45, 12, 67, 34, 89, 15, 78, 56, 90, 11, 43]

# a feladat:
szamok.sort()
print(szamok)

# b feladat:
min_index = 0
max_index = 0
for i in range(1, len(szamok)):
    if szamok[i] > szamok[max_index]:
        max_index = i
    if szamok[i] < szamok[min_index]:
        min_index = i

print("A legkisebb szám:", szamok[min_index])
print("A legnagyobb szám:", szamok[max_index])

# c feladat:
összeg = 0
for szam in szamok:
    összeg += szam
atlag = összeg / len(szamok)
print("A számok átlaga:", round(atlag, 2))

# d feladat:
parosak = [szam for szam in szamok if szam % 2 == 0]
print(parosak)


# e feladat:
szamok = tuple(szamok)
print(szamok)
#szamok[0] = 8 # TypeError: 'tuple' object does not support item assignment