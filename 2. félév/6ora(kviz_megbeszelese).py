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
# break return continue pass

# ciklusok else ága