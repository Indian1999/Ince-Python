import os
import random

def alapok(): # ctrl + alt + lefele nyíl
    ember = {
        "height": 185,
        "weight": 88.9,
        "glasses": False,
        "name": "John Doe",
        "hourly_wage": 13.89,
        "hourly_wage": 88.9 # 1 kulcs csak 1-szer szerepelhet, ez felülírja az előző sort
    } 
    # Egy érték természetesen többször is szereplhet
    #print(ember[0]) # KeyError: 0
    print(ember["name"]) # John Doe

    print(ember.keys())   # Visszaadja a kulcsokat
    print(ember.values()) # Visszaadja a tárolt értékeket
    print(ember.items())  # Visszaadja a kulcs-érték párokat

    for value in ember.values():
        print(value)
    # Ez a legrosszabb megoldás, mert értékekből nem tudjuk megkapni a kulcsokat

    for key in ember.keys():
        print(key, "->", ember[key])

    for pair in ember.items():
        print(pair)

    for key, value in ember.items():
        print(key, value)

def termekek_feladat():
    path = os.path.dirname(__file__)
    path = os.path.join(path, "termekek.txt") 
    #print(path) 

    with open(path, "r", encoding="utf-8") as f:
        data = f.read().split("\n")

    termek_count = {}
    for termek in data:
        if termek in termek_count.keys():
            termek_count[termek] += 1
        else:
            termek_count[termek] = 1

    for item in termek_count.items():
        print(item)

    termekek_rendezett = list(termek_count.items())
    termekek_rendezett.sort(key = lambda x: x[1], reverse=True)
    termekek_rendezett = dict(termekek_rendezett)
    print(termekek_rendezett)

random.seed(42)
emberek = []
for i in range(50): # 50 ember lesz
    ember = {
        "money": random.randint(100, 55000),
        "age": random.randint(18, 90),
        "profession": random.choice(["Programmer", "Receptionist", "Doctor", "Vet", "Dentist", "Telemarketer", "Carpenter", "Electrician", "Unemployed", "Engineer"])
    }
    emberek.append(ember)

# 1. feladat: Mennyi az összes ember átlagos életkora?

# 2. feladat: Mennyi csak a Programmer -ek áltlagos életkora

# 3. feladat: Hány Receptionist van aki 30000 fölötti pénzzel rendelkezik?

# 4. feladat: Mennyi pénzük van a Doctor, Vet és Dentist embereknek összesen együttvéve