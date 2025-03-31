# Dictionary (Szótár) adatszerkezet
# kulcs - érték párokat tárol

dict = {} # Üres dictionary

print(dict)
print(type(dict))

# Elemek hozzáadása
dict["cica"] = "cat" # a cica kulcshoz tartozó érték, legyen cat
dict["kutya"] = "dog"
dict["boci"] = "cow"
dict["kutya"] = "hound" 
# Mivel a kutya már szerepelt a szótárban, a hozzá tartozó értéket felül írtuk
print(dict) # 3 kulcs-érték pár 

# A kulcsok és értékek típusa lehet szinte bármi
dict[7] = True
dict[False] = [1,2,3]
dict[3.14] = {"cat": 16}
print(dict)

# Dictionary-k bejárása:

# 1. módszer: A kulcsokon megyünk végig
for key in dict.keys():
    print(key, "->", dict[key])
    
# 2. módszer: Mennyünk végig az értékeken
for value in dict.values():
    print(value)

# Érték alapján nem tudjuk lekérdezni a kulcsokat, de kulcsok alapján megkaphatjuk az érékeket
# A kulcsok egy dictionary-ben egyedi értékek, de az értékek ismétlődhetnek

# 3. módszer: A kulcs-érték párokon mennyünk végig
for item in dict.items():
    print(item, item[0], item[1])
    
for key, value in dict.items():
    print(f"key: {key}, value: {value}")
    

days_of_the_week = {
    1: "Hétfő",
    2: "Kedd",
    3: "Szerda",
    4: "Csütörtök",
    5: "Péntek",
    6: "Szombat",
    7: "Vasárnap"
}
print(days_of_the_week)

days_of_the_week_reveresed = {}
for key in days_of_the_week.keys():
    days_of_the_week_reveresed[days_of_the_week[key]] = key
    
print(days_of_the_week_reveresed)


    
