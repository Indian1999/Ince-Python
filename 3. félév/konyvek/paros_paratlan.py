a = int(input("1. szám: "))
b = int(input("2. szám: "))
c = int(input("3. szám: "))

paratlan_szamlalo = a%2 + b%2 + c%2
paros_szamlalo = 3 - paratlan_szamlalo

""" B verzió
paros_szamlalo = 0
paratlan_szamlalo = 0

if a % 2 == 0:
    paros_szamlalo += 1
else:
    paratlan_szamlalo += 1
if b % 2 == 0:
    paros_szamlalo += 1
else:
    paratlan_szamlalo += 1
if c % 2 == 0:
    paros_szamlalo += 1
else:
    paratlan_szamlalo += 1
"""
print("Párosak száma:", paros_szamlalo)
print("Páratlanok száma:", paratlan_szamlalo)
