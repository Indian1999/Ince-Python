import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("2. félév/12ora/library.csv")
data = data.drop(columns = ["Edition Statement", "Contributors", 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver', 'Issuance type', 'Flickr URL', 'Shelfmarks'])

print("Identifier is unique:", data["Identifier"].is_unique) # True -> használhajtuk inexként (kulcsként)
print("Place of Publication is unique:", data["Place of Publication"].is_unique) # False

data = data.set_index("Identifier")

# az extract függvény első paramétere egy reguláris kifejéz (egy minta [pattern])
# Ennek a paraméternek kell megadni, hogy milyen mintára illeszkedő substringet (részszöveget)
# szedjünk ki az oszlopból
# Ezt a mintát egy reguláris kifejezéssel (regular expression [regex]) tudjuk leírni
# ()    - ami a zárójelen belül van, azt kimentjük, vissza lesz adva a years df-be
# \d    - digit, 1 számjegyet azonosít
# {4}   - a \d után van -> 4 darab számjegy kell hogy egymás mellet legyen
# Ha van a stringben 4 számjegy egymás mellett, akkor azt a négy számjegyet visszaadja
years = data["Date of Publication"].str.extract(r"(\d{4})")
print(years)
print(years[0].isna().sum()) # 59 nan/null érték szerepel az oszlopan (59 könyvnek nem ismerjük a kiadási dátumát)
"""
A Nan értékek problémákhoz vezethetnek adatelemzésnél, ilyenkor választanunk kell egy módszert
amivel ezeket lekezeljük
"""
"""
1. módszer: Legyen -1 minden NaN érték
# Azért, hogy intté tudjuk konvertálni, töltsük fel a nan értékeket egy számmal
# Ha egy érték NaN, akkor legyen 9999, -1, -1000
years[0] = years[0].fillna(-1)
print(years[0].isna().sum()) # 0 -> feltöltöttók a nan értékeket -1, úgyhogy már nincs 1 nan se
data["Date of Publication"] = years[0].astype(int)
print(data.head())
"""

"""
2. módszer: A NaN értékeket állítsuk be az oszlop átlag értékére
average = round(pd.to_numeric(years[0]).mean()) # 1859
print(average)
years[0] = years[0].fillna(average)
data["Date of Publication"] = years[0].astype(int)
print(data.head())
"""

"""
3. módszer: Töröljük a NaN értékeket
"""
data["Date of Publication"] = pd.to_numeric(years[0])
data = data.dropna(subset=["Date of Publication"])
print(data["Date of Publication"].isna().sum())
data["Date of Publication"] = data["Date of Publication"].astype(int)
print(data)

# Mostmár a Date of Publication oszlop tiszta adatokat tartalmaz



#####################################################
#         Place of Publication tisztítása           #
#####################################################

unique_places = data["Place of Publication"].value_counts()
print(unique_places.head(15))
"""
london = data["Place of Publication"].str.contains("London")
paris = data["Place of Publication"].str.contains("Paris")
edinburgh = data["Place of Publication"].str.contains("Edinburgh")
new_york = data["Place of Publication"].str.contains("New York")
leipzig = data["Place of Publication"].str.contains("Leipzig")
philadelphia = data["Place of Publication"].str.contains("Philadelphia")
berlin = data["Place of Publication"].str.contains("Berlin")

data["Place of Publication"] = np.where(london, "London", data["Place of Publication"])
"""
def find_substring_and_replace(data, city):
    try:
        city_list = data["Place of Publication"].str.contains(city)
        data["Place of Publication"] = np.where(city_list, city, data["Place of Publication"])
    except:
        print("Hiba a következő város keresésénél:", city)
        pass # Ez a kód akkor fut le, amikor a try blokkban hiba lépet
    
st_petersburg = data["Place of Publication"].str.contains("Петербург")
data["Place of Publication"] = np.where(st_petersburg, "St. Petersburg", data["Place of Publication"])

for city, count in unique_places.items():
    find_substring_and_replace(data, city)
    if count < 3:
        break

unique_places = data["Place of Publication"].value_counts()
print(unique_places.head(30))

data.to_csv("2. félév/12ora/library_clean.csv")