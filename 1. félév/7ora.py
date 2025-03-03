#Ismétlés
print("Hello World!")
#szöveg = input("Add meg a neved!\n")
#print("Hello " + szöveg + "!")

egész_szám = 5
lebegőpontos_szám = 3.14
logikai_érték = True
szöveg = "Sanyi"

lista = [1,7,4,3,7,9,5,3,1,3]
lista[2]
lista[7] = 0
lista[6] *= 2
lista[-1] #utolsó elem
lista[-2] #Hátulról a második

print(lista[3:7])
print(lista[:5])
print(lista[3:])
print(lista[:])

for i in range(10):
    print(i)

print()
for i in lista:
    print(i)

while len(lista) < 15:
    lista.append(0)

print(lista)

összeg = 0
for item in lista:
    összeg += item

print(összeg)

#Szöveg kódolások
#Minden második betű kód
# Leesett az alma az almafáról
# Leeta laa laáóest zam zamfrl

szöveg = "Leesett az alma az almafáról"
kódolt_szöveg = ""
for i in range(0, len(szöveg), 2):
    kódolt_szöveg += szöveg[i]
for i in range(1, len(szöveg), 2):
    kódolt_szöveg += szöveg[i]

print(kódolt_szöveg)


#Caesar kód

szöveg = "d nlvnxwbd vchuhw xjdwql" #d nlvnxwbd vchuhw xjdwql A kiskutya szeret ugatni
abc = "abcdefghijklmnopqrstuvwxyz"

szöveg = szöveg.lower()
kódolt_szöveg = ""
for char in szöveg:
    if char in abc:
        index = abc.index(char)
        kódolt_szöveg += abc[(index - 3) % 26]
    else:
        kódolt_szöveg += char
    
print(kódolt_szöveg)

#Gyakorló feladatok:

lista = [19, 28, -33, 81, 0, 12, -16, 9, 10, 4, 5, 19, 8, 19, -3, 7, 9, 12, 67]

#Határozzuk meg a lista elemeinek az összegét

#Határozzuk meg a számok átlagát

#Határozzuk meg a pozitív számok összegét

#Határozzuk meg a negatív számok összegét

#Határozzuk meg a legkisebb számot

#Határozzuk meg a legnagyobb számot

#Rendezzük a listát

# Egyszerű cserés rendezés
össszehasonlítások = 0
cserék = 0
for i in range(0, len(lista)-1):
    for j in range(i + 1, len(lista)):
        össszehasonlítások += 1
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i] # Megcseréli a két elemet
            cserék += 1

print(lista)
print("Cserék:", cserék)
print("Össszehasonlítások:", össszehasonlítások)

lista = [19, 28, -33, 81, 0, 12, -16, 9, 10, 4, 5, 19, 8, 19, -3, 7, 9, 12, 67]

#Buborékos rendezés

össszehasonlítások = 0
cserék = 0
for i in range(len(lista) - 1, 0, -1):
    for j in range(0, i):
        össszehasonlítások += 1
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j] # CSERE
            cserék += 1
            
print(lista)
print("Cserék:", cserék)
print("Össszehasonlítások:", össszehasonlítások)




