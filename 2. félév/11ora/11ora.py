import csv
import pandas as pd # terminálba: pip install pandas
import matplotlib.pyplot as plt # pip install matplotlib.pyplot

file = open("2. félév/11ora/oscar_age_female.csv")

data = csv.reader(file, delimiter = ",")
print(data) # <_csv.reader object at 0x000001D3680E72E0>
for row in data:
    print(row)

file.close()


data = pd.read_csv("2. félév/11ora/oscar_age_female.csv")
print(data)
print(type(data)) # <class 'pandas.core.frame.DataFrame'> DataFrame
print(data.head(10)) # első 10 sor

# Mennyi volt a nyertesek átlag életkora?
print("A nyertesek átlag életkora:", round(data["Age"].mean()) )
print("A legfitalabb nyertes életkora:", data["Age"].min())
print("A legidősebb nyertes életkora:", data["Age"].max())
print("Az életkorok mediánja:", data["Age"].median())
print("Az életkorok szórása:", data["Age"].std())

# Ki volt a legidősebb nyertes?
eldest = data[data["Age"] == data["Age"].max()]
print(eldest) # DataFrame
eldest_name = eldest["Name"].iloc[0].strip().replace('"', '')
eldest_age = eldest["Age"].iloc[0]
print(f"A legidősebb nyertes {eldest_name} volt. {eldest_age} évesen kapta a díjat.")

# Keressük meg, hogy mikor nyert a Fargo című film!
találatok = data[data["Movie"].str.contains("Fargo")]
fargo_year = találatok["Year"].iloc[0]
print(f"A Fargo című film {fargo_year}-ben nyert Oscar díjat.")

# Ki nyerte a legtöbb díjat?
counts = data["Name"].value_counts()
print(counts)
print(type(counts)) # <class 'pandas.core.series.Series'>
most_frequent_name = counts.idxmax()
most_frequent_name = most_frequent_name.strip().replace('"', '')
frequency = counts.max()

print(f"A legtöbb díjat {most_frequent_name} kapta. Összesen {frequency} alkalommal nyert.")

# Ábrázoljuk Scatter-ploton az évszám és az életkorok relációját
plt.scatter(x = data["Year"], y = data["Age"])
plt.title("Női Oscar Díjasok Évszám-Életkor összehasonlítása")
plt.xlabel("Évszám")
plt.ylabel("Életkor")
plt.savefig("2. félév/11ora/oscar_age_female_scatter.png")
plt.close()

# Ábrázoljuk kördiagrammon, hogy az egyes életkorok, hány alkalommal nyertek díjat
counts = data["Age"].value_counts()
counts = counts.head(10)

#len(explode_list) == len(counts)
explode_list = [0.1 for i in range(10)]
#explode_list[0] = 0.1

plt.pie(counts, labels=counts.index, explode=explode_list, autopct="%1.1f%%")
plt.title("Nyertesek életkorának gyakorisága")
plt.savefig("2. félév/11ora/oscar_age_female_frequency.png")
plt.close()

# Határozzuk meg hogy milyen sűrűn fordulnak elő a magánhangzók!

letters = pd.read_csv("2. félév/11ora/letter_frequency.csv", skipinitialspace=True)
vowels = "AEUIO"
vowel_pct = 0
for index, row in letters.iterrows():
    if row["Letter"] in vowels:
        vowel_pct += row["Percentage"]
print(f"A betűk {round(vowel_pct,1)} %-a magánhangzó.")
