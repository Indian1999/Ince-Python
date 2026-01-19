# 7. feladat: Számkitaláló játék
import random

puzzle = random.randint(1, 1000)
print("Gondoltam egy számra 1-1000 között, próbáld meg kitalálni!")

for i in range(1, 11):
    tipp = int(input("Tipllej egy számot: "))
    if tipp < puzzle:
        print("Ettől nagyobb számra gondoltam!")
    elif tipp > puzzle:
        print("Ettől kisebb számra gondoltam")
    else:
        print(f"Gratulálok! A szám valóban a {puzzle} volt.")
        print(f"{i} lépésből találtad ki!")
        break
else: # Akkor fut le, ha NEM break-kel lépünk ki
    print(f"Vesztettél! A gondolt szám a {puzzle} volt.")
