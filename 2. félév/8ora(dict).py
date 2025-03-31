# Dictionary (Szótár) adatszerkezet
# kulcs - érték párokat tárol

szotar = {} # Üres dictionary

print(szotar)
print(type(szotar))

# Elemek hozzáadása
szotar["cica"] = "cat" # a cica kulcshoz tartozó érték, legyen cat
szotar["kutya"] = "dog"
szotar["boci"] = "cow"
szotar["kutya"] = "hound" 
# Mivel a kutya már szerepelt a szótárban, a hozzá tartozó értéket felül írtuk
print(szotar) # 3 kulcs-érték pár 

# A kulcsok és értékek típusa lehet szinte bármi
szotar[7] = True
szotar[False] = [1,2,3]
szotar[3.14] = {"cat": 16}
print(szotar)

# Dictionary-k bejárása:

# 1. módszer: A kulcsokon megyünk végig
for key in szotar.keys():
    print(key, "->", szotar[key])
    
# 2. módszer: Mennyünk végig az értékeken
for value in szotar.values():
    print(value)

# Érték alapján nem tudjuk lekérdezni a kulcsokat, de kulcsok alapján megkaphatjuk az érékeket
# A kulcsok egy dictionary-ben egyedi értékek, de az értékek ismétlődhetnek

# 3. módszer: A kulcs-érték párokon mennyünk végig
for item in szotar.items():
    print(item, item[0], item[1])
    
for key, value in szotar.items():
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

f = open("2. félév/rubik.txt", "r", encoding = "utf-8")
szöveg = ""
sorok = f.readlines()
for sor in sorok:
    szöveg += sor.strip() 
    # A strip az elejéről és a végéről levágja a szóközeket és az entereket
    szöveg += " "
f.close()

szöveg = szöveg.lower()
print(szöveg)

szavak = szöveg.split(" ") # A szöveget daraboljuk fel szóközek mentén
# ez egy stringekből álló listát fog eredményezni

word_count = {}
for word in szavak:
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 1
        
print(word_count)

# Dictionary rendezése
print(sorted(word_count)) # Egy lista a szavakról abc sorrendben
word_count = dict(sorted(word_count.items(), key=lambda x: x[1], reverse=True))
print(word_count)


# Feladat: Olvassuk be az autok.txt file-t és egy dictionary-be számoljuk össze, 
# hogy melyik márkából hány szerepel a fileban

brands = []

f = open("2. félév/autok.txt", "r", encoding="utf-8")
for line in f:
    brands.append(line.strip())
f.close()

brand_count = {}
for item in brands:
    if item in brand_count.keys():
        brand_count[item] += 1
    else:
        brand_count[item] = 1
        
brand_count = dict(sorted(brand_count.items(), key=lambda x: x[1], reverse=True))
print(brand_count)
    
