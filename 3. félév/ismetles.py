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