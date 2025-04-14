import random

myDict = {
    "alma": 9,
    "banán": 17,
    "citrom": 3,
    "dinnye": 9 
}
print(myDict)

# Egy Dictionary-t bejárhatunk kulcsonként, értékekklnt, vagy kulcs-érték páronként

for key in myDict.keys(): # A key ciklusváltozó sorban felveszi a kulcsokat
    print(key, "->", myDict[key]) # Kulcs alapján meg tudjok nézni a hozzá tartozó értéket is
    
for value in myDict.values(): # A value ciklusváltozó sorban felveszi a myDict értékeit (9, 17, 3, 9)
    print(value) # Az értékekből nem tudjuk kinyerni a kulcsokat
    
for pair in myDict.items(): # A pair ciklusváltozó sorban felveszi a myDict kulcs-érték párjait
    print(pair)
    print(type(pair)) # tuple típusú objektum
    print("pair[0]:", pair[0]) # kulcs
    print("pair[1]:", pair[1]) # érték
    
# A Tuple adatszerkezet
# A tuple szinte teljesen ugyan az mint a lista, annyi a különbség, hogy a tuple az nem móddosítható 
# (non mutable)

myTuple = (5, 9, 1, 6) # 4 elemű tuple ami inteket tárol
print(myTuple)
print(type(myTuple))
print(id(myTuple))

# Mit NEM csinálhatunk?
#myTuple.append(6)  # AttributeError  'tuple' object has no attribute 'append'
#myTuple[2] = 7     # TypeError       'tuple' object does not support item assignment

# Mi van akkor, ha minden áron a 2-es indexű elemet 7-re szeretném változtatni?
# Itt nem egy számot írunk át, hanem a teljes tuple-t újradefiniáljuk
myTuple = (5, 9, 7, 6)
print(id(myTuple)) # Miután újradefiniáltuk, ezért új memóriacímre is került
print(myTuple)

# Ha jobban megkötjük a kezünket, akkor kisebb eséllyel fordulnak elő hibák

myTupleZeroElems = ()
print(myTupleZeroElems) # () 0 elemű tuple
print(type(myTupleZeroElems)) # <class 'tuple'>

myTupleOneElem = (5)
print(myTupleOneElem) # 5
print(type(myTupleOneElem)) # <class 'int'>
# Tapasztalat: int-ként hozta létre
# Magyarázat: a zárójeleket itt aritmetikai jelölésként értelmezte a python interpreter

myTupleOneElem = (5,) # ,-vel jelölöm, hogy ez nem egy aritmetikai kifejezés
print(myTupleOneElem) # (5,)
print(type(myTupleOneElem)) # <class 'tuple'>

# Tuple-t vagy listát használjak?
# Ha sok elem van, ezek változhatnak, az elemek szám is változhat -> lista
# Ha bonyolultabb elemekt tárolunk el (osztály példányt) -> lista
# Ha csak néhány elem van, ezek nem változhatnak, fix darabszám -> tuple

item = ("mangó", 16)
key, value = item
print(key)
print(value)

myTuple = (54, 12, 9, 3)

elso, masodik, harmadik, negyedik = myTuple
print(elso, masodik, harmadik, negyedik)

# feladat: írjunk egy függvényt, ami egy 2D-s mátrixban megkeres egy adott értéket és visszaadja
# a sor-oszlop indexeket

def find_in_matrix(matrix, value):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == value:
                return (i,j)
    return None # Ha nem találtunk ilyen értéket, None értékkel lépünk ki

matrix = [[random.randint(1, 100) for j in range(8)] for i in range(10)]      
for row in matrix:
    print(row)  
    
print(find_in_matrix(matrix, 50))

# Kicsit profibb megoldás: Ne egy konkrét értéket keressünk, hanem egy adott feltételt kielégitőt
# a függvénynek egy valamilyen másik függvényt adunk át paraméterül

def find_in_matrix_2(matrix, func):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if func(matrix[i][j]):
                return (i,j)
    return None # Ha nem találtunk ilyen értéket, None értékkel lépünk ki

def greater_than_90(x):
    return x > 90

def divisible_by_37(x):
    return x % 37 == 0

def digit_sum_is_15(x):
    digit_sum = 0
    for char in str(x):
        digit_sum += int(char)
    return digit_sum == 15

print(find_in_matrix_2(matrix, greater_than_90))
print(find_in_matrix_2(matrix, divisible_by_37))
print(find_in_matrix_2(matrix, digit_sum_is_15))

# Ezzel egy probléma van, létrehoztunk függvényeket amiket csak egyszer használunk
# Rondítják a kódot fölöslegesen (Nem szükséges elmenteni a greater_than_90 függvényt)
# Ennek elkerülése érdekében használhatunk lamba függvényeket
print(find_in_matrix_2(matrix, lambda x: x > 90)) # Ugyan azt valósítja meg, mint a greater_than_90 függvény
print(find_in_matrix_2(matrix, lambda x: len(str(x)) == 1)) # 1 jegyű számot keres
print(find_in_matrix_2(matrix, lambda x: x == 5)) # konkrétan az 5-öt


    