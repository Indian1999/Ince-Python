# Beolvasunk kettő dátumot: az egyik az a mai dátum
# A másik, pedig valakinek a születési dátuma
# Ezek alaphán, hány napos az ember
mai_datum = "2025-01-06"
#           "2025-02-06"
#szuletes_nap = input("Add meg a születésnapodat! (pl.: 1999-02-10)\n")
szuletes_nap = "2025-01-01"
today = mai_datum.split("-")   # "2025-01-06" -> ["2025", "01", "06"]
today = [int(num) for num in today] # az összes elemet számmá konvertáljuk

birthday = szuletes_nap.split("-")
birthday = [int(num) for num in birthday]

honapok = ["nulladik elem", 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = 0

def is_leap_year(evszam):
    if evszam % 400 == 0:
        return True
    if evszam % 100 == 0:
        return False
    if evszam % 4 == 0:
        return True
    return False

while today != birthday:
    if birthday[2] < honapok[birthday[1]]:
        birthday[2] += 1
    else:
        if birthday[1] == 2 and is_leap_year(birthday[0]) and birthday[2] == 28:
            birthday[2] += 1
        elif birthday[1] == 12:
            birthday[0] += 1
            birthday[1] = 1
            birthday[2] = 1
        else:
            birthday[1] += 1
            birthday[2] = 1
    days += 1
    #print(birthday)

print(days)

# 2. feldat: döntsük el két stringről, hogy egymás anagrammáik-e!
# Amy - May
#first = input("Add meg az első szót!\n")
#second = input("Add meg a második szót!\n")
first = "Amy"
second = "May"
first = first.lower() # kisbetűssé alakítja
second = second.lower()

if sorted(first) == sorted(second):
    print("Ezek egymás anagrammái")
else:
    print("Ezek nem egymás anagrammái")


# 3. feladat: értékeljünk ki egy szavazást!
színek = ["piros", "kék", "sárga", "fekete", "fehér", "zöld"]
szavazatok = [132, 124, 141, 143, 97, 136]

# Hány színre lehett szavazni?
print(f"A szavazás során {len(színek)} színre lehetett szavazni.")

# Az egyes színek hány szavazatot kaptak?

for i in range(len(színek)):
    print(f"{színek[i]} - {szavazatok[i]} szavazat")

# Melyik szín lett a nyertes?

# Összesen hány szavazat érkezett?

# 4. feladat: Hány autónak kell lelassítania?
autok = [45, 83, 12, 35, 78, 54, 32, 67, 78, 90, 82, 81, 83, 85, 100, 77]

számláló = 0
for i in range(len(autok)):
    leglassabb = True
    for j in range(i + 1, len(autok)):
        if autok[j] < autok[i]:
            leglassabb = False
            break
    if not leglassabb:
        számláló += 1

print(számláló, "kocsinak kell lassítania.")
















# Task 2 - finding anagrams

# Task 3 - slow down

# Task 4 - voting for new burger
burgers = ["Spicy Pinata", "Cheesy Dream", "Vegan Fluffy", "Fatty Boom", "Tortuga", "Pork Pie"]
votes = [95061, 93439, 98563, 90478, 90915, 97334]

# number of new burgers

# votes per burgers
    
# winner of the competition


# number of votes