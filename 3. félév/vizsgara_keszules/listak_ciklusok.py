lista1 = [5, 2, 8, 1]

print(lista1[0]) # 5     0. elem (0-tól számozzuk az elemeket)
lista1.append(9) # egy kilencest rak a lista végére   [5, 2, 8, 1, 9]
lista1.insert(2, 7) # A 2. indexre berakunk egy 7-est [5, 2, 7, 8, 1, 9]
lista1.remove(8) # A 8 értéknek az első előfordulását törlni [5, 2, 7, 1, 9]
del lista1[3]    # Törli a listának a 3. indexü elemét [5, 2, 7, 9]
value = lista1.pop() # Törli a lista1 utolsó elemét, és a value-ba elmemnti [5, 2, 7]
print(value) # 9
value = lista1.pop(1) # 1-es indexű elemet törli és adja vissza [5, 7]
print(value) # 2
lista1 = lista1 + [1,2,3,4]
print(lista1) # [5, 7, 1, 2, 3, 4]
lista1 += [9, 1]
print(lista1) # [5, 7, 1, 2, 3, 4, 9, 1]

szamok = lista1

szamok.remove(1)
szamok.append(99)

print(lista1)
print(szamok) # Tapasztalat, a szamok módosításával, mind a két lista változott

szamok = lista1[:] # Ilyenkor másolat fog készülni

szamok.append(7)
print(lista1)
print(szamok) # Mostmár különbözik a két lista

print(szamok[3:6]) # 3-as indextől a 6. indexig (6. már nincs benne)
# [3, 4, 9]
print(szamok[:5]) # Elejétől a 5. indexig (5. nincs benne)
# [5, 7, 2, 3, 4]
print(szamok[4:]) # A 4. indextől a legvégéig
# [4, 9, 1, 99, 7]
print(szamok[:])
# [5, 7, 2, 3, 4, 9, 1, 99, 7]


szamok = [5, 7, 2, 3, 4, 9, 1, 99, 7]

for item in szamok:
    if item % 5 == 2:
        continue
    print("#")

# Hány #-t ír ki ez a program (6)


szamok = [5, 7, 2, 3, 4, 9, 1, 99, 7]

for i in range(szamok[5]):
    if i in szamok:
        print('#')

# Hány #-t ír ki ez a program (6)


szamok = [5, 7, 2, 3, 4, 9, 1, 99, 7]

value = szamok.pop()
for item in szamok:
    if item >= value:
        print("#")

# Hány #-t ír ki ez a program (3)



# A ciklusok else ága lefut mindig, ha nem break-el léptünk ki a ciklusból
for i in range(5):
    print(i)
else:
    print("Ciklus else ága")

while False:
    pass
else:
    print("While else ága")

for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("Ez az else ág nem fog lefutni")




for i in range(3, 13, 2):
    if i % 5 == 0:
        print("#")
    if i % 2 == 0:
        break
else:
    print("#")

# Hány #-t ír ki ez a program (2)


print()

for i in range(3, 8):
    if i > 5:
        break
    print("#")
else:
    print("#")

# Hány #-t ír ki ez a program (3)





# Feladat: Írjunk egy programot ami kirajzolja a következő alakzatot:
"""
_____#_____        5: _ 1 db # 5 _
____###____         4 _ 3 # 4 _
___#####___         3 _ 5 # 3 _
__#######__         2 _ 7 # 2 _
_#########_
###########
_____#_____
_____#_____
"""

n = 15
for i in range(1, n + 1):
    print(" " * (n-i),    (i*2 - 1) * "#",    " " * (n-i), sep="")
for i in range(2):
    print(" " * (n-1),    "#",    " " * (n-1), sep="")

print("     #     ")
print("    ###    ")
print("   #####   ")
print("  #######  ")
print(" ######### ")
print("###########")
print("     #     ")
print("     #     ")






