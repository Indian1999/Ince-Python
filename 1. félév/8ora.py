"""
import random
puzzles = ["lion king", "finding nemo", "despicable me", "monster university", "frozen", "rio", "walle", "incerdibles", "sponge bob", "tom and jerry", "turning red", "finding dory", "shrek", "how to train your dragon", "inside out", "asterix and obelix", "the little mermaid", "cinderella", "tangled", "phineas and ferb", "kim possible", "samurai jack", "johny bravo", "pocahontas"]
puzzle = puzzles[random.randrange(0, len(puzzles))]
# randrange(0, 10)      0 és 9 között generál egy random számot
my_solution = ""
for char in puzzle:
    if char == " ":
        my_solution += " "
    else:
        my_solution += "*"
life = 10
correct_letters = []
wrong_letters = []
while life > 0 and my_solution != puzzle: # Amíg tart a játék
    print(my_solution)
    char = input("Tippelj egy betűt!\n").lower()
    if len(char) == 1:
        found = False
        for i in range(len(puzzle)):
            if puzzle[i] == char:
                found = True
                lista = list(my_solution)
                lista[i] = char
                my_solution = "".join(lista)
        if found:
            correct_letters.append(char)
        else:
            wrong_letters.append(char)
            life -= 1
            print(f"Sajnos ez a betű nem szerepel a feladványban, még {life} életed maradt.")
        print("Kitalált betűk", correct_letters)
        print("Rossz betűk", wrong_letters)
    else:
        if char == puzzle:
            print("Eltaláltad!")
            my_solution = char
        else:
            life -= 1
            print(f"Nem ez a megoldás! Még {life} életed maradt.")
if life > 0:
    print("Gratulálok!")
else:
    print("Talán legközelebb...")

print("Megoldás:", puzzle)
"""

#Mátrixok - táblázat (listák amik listákat tárolnak)
mtx = [
    [1, 2, 3],
    [2, 4, 5],
    [8, 3, 9]
]
print(mtx)
print(mtx[1]) # [2, 4, 5]
print(mtx[0][2]) # 3
mtx[2][2] = 6
print(mtx)

for i in range(len(mtx)):
    print(mtx[i])
    for j in range(len(mtx[i])):
        print(mtx[i][j])

#Összegzés tétele mátrixokra:
összeg = 0
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        összeg += mtx[i][j]

print("Összeg =", összeg)

#Határozzuk meg a legnagyobb elemet a mátrixban

maximum = mtx[0][0]
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        if mtx[i][j] > maximum:
            maximum = mtx[i][j]

print("A legnagyobb elem:", maximum)

#Adjuk össze a páros számokat

#Számoljuk ki a mátrix elemeinek az átlagát


