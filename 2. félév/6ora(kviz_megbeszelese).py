# stringek szorzása

szöveg = "kiskutyka"
print(szöveg * 3) #kiskutykakiskutykakiskutyka

# listák indexelése, egyik elem egyenlővé tétele a másikkal

lista = [1,2,3,4,5,6,7,8]
print(lista[0])     # 1
print(lista[5])     # 6
print(lista[-1])    # 8
print(lista[-5])    # 4
print(lista[2:6])   # [3,4,5,6]
print(lista[:4])    # [1,2,3,4]
print(lista[5:])    # [6,7,8]
print(lista[::-1])  # [8,7,6,5,4,3,2,1]
print(lista[0:5:2]) # [1,3,5]  0-tól 5-ig, 2-esével lépkedve

# myList[myList[-1]]

print(lista[lista[-2]])         #lista[-2]: 7 -> lista[7] -> 8
print(lista[lista[lista[-6]]])  #lista[-6]: 3 -> lista[3]: 4 -> lista[4] -> 5

# listák egyenlővé tétele egymással

# Amikor egy listát egyenlővé teszünk egy másik listával, akkor nem jön létre másolat a memóriában,
# hanem az új lista, ugyan arra a fizai memória címre fog mutatni
# -> Ugyan arra az 1 listára két különböző változóval mutatunk
lista_1 = [3, 0, 6, 4]
lista_2 = lista_1
print(lista_1) # [3, 0, 6, 4]
print(lista_2) # [3, 0, 6, 4]
# Ha az egyiken módosítunk valamit, akkor mind a kettő változni fog
lista_1[2] = -10
print(lista_1) # [3, 0, -10, 4]
print(lista_2) # [3, 0, -10, 4]
lista_2[0] = 0
print(lista_1) # [0, 0, -10, 4]
print(lista_2) # [0, 0, -10, 4]
del lista_1[2]
print(lista_1) # [0, 0, 4]
print(lista_2) # [0, 0, 4]

print(id(lista_1)) # 1662556369216
print(id(lista_2)) # 1662556369216 (megegyeznek)

lista_3 = lista_1[:]
lista_3[1] = 23
print(lista_1)
print(id(lista_1))
print(lista_2)
print(id(lista_2))
print(lista_3)
print(id(lista_3))

# list comprehension
lista = [0 for i in range(5)]
print(lista)  # [0,0,0,0,0]
lista = [i for i in range(10, 100, 20)] # [10, 30, 50, 70, 90]
print(lista)
#A range függvény egy generátor függvény (elemeket sorol fel)
lista = list(range(5)) 
print(lista)
# egy ilyen felsorolót, listává tudunk alakítani

lista = [i**2 - 8*i + 16 for i in range(0, 9)]
print(lista)
lista = [[] for i in range(5)]
print(lista)
lista = [[1,2,3,4] for i in range(4)]
print(lista) 
lista = [[i for i in range(-6, 19, 7)] for j in range(5)]
print(lista)
lista = [[[k for k in range(5)] for j in range(3)] for i in range(6)]
print(lista)

# pass kulcsszó
# Nem csinál semmit

def func(x):
    pass

func(5) # Nem történik semmi

# Erre azért van szükség mert ha egy blokk belsejébe nem írunk írunk semmit, akkor hibát kapunk

# break
# Kilép az aktuálisan futó ciklusból

for i in range(10):
    if i == 3:
        break # kilép a ciklusból, az aktuális ciklus iteráció se fog végig menni (3-at már nem írjuk ki)
    print(i)

for i in range(10):
    for j in range(8):
        if j == 2:
            break # Ha két ciklus fut, csak a belsőből lépünk ki
        print(f"j = {j}")
    print(f"i = {i}")

# continue
# Ha ez a kulcsszót használjuk, akkor az aktuális ciklus iterációt átugorjuk és a következőre megyünk
for i in range(10): # 0 2 4 6 8
    if i % 2 != 0:
        continue #Minden ami ez után van, nem fut le (páratlan számok nem lesznek kiírva)
    print(i, end = " ")
print()

# ciklusok else ága
# Akkor fut le, ha NEM break-kel léptünk ki a ciklusból

for i in range(5):
    print("#")
else:
    print("lefutott az else ág") # nem breakkel léptünk ki -> lefut
    
for i in range(5):
    if i == 2:
        break
else:
    print("Ez itt az else ág") # nem fut le, mert break-kel léptünk ki
    
# Akkor is lefut az else ág, ha egyszer sem fut le a ciklus

game_on = False
while game_on:
    print("szia")
else:
    print("Egyszer sem fut le, mégis itt vagyunk az else ágban.") # Le fog futni