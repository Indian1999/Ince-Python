# a feladat:

gyumolcsok = {
    "alma": 99,
    "banán": 179,
    "citrom": 149,
    "dinnye": 789,
    "mandarin": 129,
    "avokadó": 349
}
print(gyumolcsok)

# b feladat:
gyumolcs = input("Add meg egy gyümölcs nevét: ")
if gyumolcs in gyumolcsok.keys():
    print(f"{gyumolcs} - {gyumolcsok[gyumolcs]} Ft")
else:
    print("Ez a gyümölcs nem található.")

# c feladat:
gyumolcsok["narancs"] = 199

# d feladat:
for key, value in gyumolcsok.items():
    print(f"{key}: {value} Ft")

# e feladat:
halmaz1 = set(gyumolcsok.keys())
halmaz2 = set(["alma", "banán", "mandarin", "szőlő", "körte", "papaya"])

print(f"A halmaz:", halmaz1)
print(f"B halmaz:", halmaz2)

print(f"Unió: {halmaz1.union(halmaz2)}")
print(f"Metszet: {halmaz1.intersection(halmaz2)}")

