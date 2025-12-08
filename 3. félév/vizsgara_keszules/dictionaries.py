import os

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

path = os.path.dirname(__file__)
path = os.path.join(path, "termekek.txt") 
#print(path) 

with open(path, "r", encoding="utf-8") as f:
    pass
