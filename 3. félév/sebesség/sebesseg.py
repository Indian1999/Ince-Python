import os

def beolvas(path):
    with open(path, "r", encoding="utf-8") as f:
        length = int(f.readline().strip())
        distances = []
        speed_limiters = []
        sor = f.readline()
        while sor != "":
            sor_adatok = sor.strip().split(" ")
            distances.append(int(sor_adatok[0]))
            speed_limiters.append(sor_adatok[1])
            sor = f.readline()
    return length, distances, speed_limiters

def at_least_4_chars(lista: list[str]):
    for item in lista:
        if len(item) >= 4:
            yield item

def limit_string_to_kph(limit_string, in_city: bool):
    if limit_string.isdigit(): # számot tárol a string
        return int(limit_string)
    if len(limit_string) >= 4: # Városba értünk
        return 50
    if limit_string == "]": # Kiértünk a városból
        return 90
    if limit_string == "%" or limit_string == "#": # Feloldjuk a sebességkorlátozást
        if in_city:
            return 50
        else:
            return 90 

def smallest_speed_limit(distances, speed_limiters, endpoint):
    smallest_speed = 90
    in_city = False
    for i in range(len(distances)):
        distance = distances[i]
        limit_string = speed_limiters[i]
        if distance > endpoint:
            return smallest_speed
        if len(limit_string) >= 4:
            in_city = True
        if limit_string == "]":
            in_city = False
        speed_limit = limit_string_to_kph(limit_string, in_city)
        if speed_limit < smallest_speed:
            smallest_speed = speed_limit
    return smallest_speed

def get_city_distances(distances, speed_limiters):
    city_start_distances = []
    city_end_distances = []
    for i in range(len(distances)):
        if len(speed_limiters[i]) >= 4:
            city_start_distances.append(distances[i])
        if speed_limiters[i] == "]":
            city_end_distances.append(distances[i])
    
    total_city_distance = 0
    for i in range(len(city_start_distances)):
        total_city_distance += city_end_distances[i] - city_start_distances[i]

    return total_city_distance

root = os.path.dirname(__file__) # Annak a mappának az elérési útvonala, amibe fut a script
length, distances, speed_limiters = beolvas(os.path.join(root, "ut.txt"))

print("2. feladat:")
print("A települések neve:")
for city in at_least_4_chars(speed_limiters):
    print(city)

print("3. feladat:")
endpoint = float(input("Adja meg a vizsgált szakasz hosszát (km-ben): "))
smallest_speed = smallest_speed_limit(distances, speed_limiters, endpoint * 1000)
print(f"Az első {endpoint} km-en a legkisebb sebességhatár {smallest_speed} km/h volt.")

print("4. feladat:")
city_percentage = get_city_distances(distances, speed_limiters) / length * 100
print(f"Az út {round(city_percentage, 2)} %-a vezet településen belül.")

def city_properties(distances, speed_limiters, city):
    counter = 0
    city_found = False
    city_start = None
    city_length = None
    for i in range(len(distances)):
        if speed_limiters[i] == city:
            city_found = True
            city_start = distances[i]
        if city_found and speed_limiters[i].isdigit():
            counter += 1
        if city_found and speed_limiters[i] == "]":
            city_length = distances[i] - city_start 
            break
    return counter, city_length


print("5. feladat:")
city = input("Add meg egy város nevét: ")
tablak, hossz = city_properties(distances, speed_limiters, city)
print(f"A sebességkorlátozó táblák száma: {tablak}")
print(f"Az út hossza a településen belül {hossz} méter.")

print("6. feladat:")
cities = []
for i in range(len(distances)):
    if len(speed_limiters[i]) >= 4:
        cityDict = {
            "name": speed_limiters[i],
            "start": distances[i]
        } 
        cities.append(cityDict)
    if speed_limiters[i] == "]":
        cities[-1]["end"] = distances[i]

city = input("Add meg egy város nevét!\n")
closest_city = None
for i in range(len(cities)):
    if cities[i]["name"] == city:
        if i != 0 and i != len(cities) - 1: # nem az első és nem az utolsó város
            prev_distance = cities[i]["start"] - cities[i-1]["end"]
            next_distance = cities[i+1]["start"] - cities[i]["end"]
            if prev_distance >= next_distance:
                closest_city = cities[i-1]["name"]
            else:
                closest_city = cities[i+1]["name"]
        elif i == 0:
            closest_city = cities[i+1]["name"]
        else:
            closest_city = cities[i-1]["name"]

if closest_city == None:
    print("Nincs az útszakaszon ilyen nevű város.")
else:
    print(f"A {city} városhoz legközelebbi város: {closest_city}")






