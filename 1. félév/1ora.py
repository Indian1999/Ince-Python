"""
print("Hello világ!")
print(5)
print()
print("Az üres print, csak egy sortörés")

print("Sajt", "Kenyér", "Szalámi")      #Sajt Kenyér Szalámi
print("Sajt" + "Kenyér" + "Szalámi")    #SajtKenyérSzalámi

print(3, 4, 5)
print(3 + 4 + 5)

num = 58

print(num)
print("A num változó értéke:", num)
print("A num változó értéke: " + str(num))

# "a" + "b" -> "ab"
# 1 + 2 -> 3
# "a" + 3 -> ERROR
# "a" + "3" -> "a3"

word = "malac"

print("word = " + word)
print(word.capitalize()) #Malac
print(word.upper()) #MALAC
print(word.replace("a", "o"))
print(word.replace("ala", "ora"))

word = input("Add meg a nevedet: ")
print("Szia " + word + "!")

num = int(input("Adj meg egy számot: "))
#Az input eredménye az mindig egy szöveg típus
if num % 2 == 0:
    print("Ez egy páros szám!")
else:
    print("Ez egy páratlan szám!")
print("Örülök, hogy segíthettem!")

"""

egész_szám = 5 # int (integer) egész számokat tárol
tört_szám = 3.14 # float - nem egész számokat is tud tárolni
szöveg = "almafa" # str (string) - karaktersorozat (szöveg)
logikai_érték = True # bool (boolean) - logikai érték (True/False)

print(egész_szám)
print(type(egész_szám))
print(tört_szám)
print(type(tört_szám))
print(szöveg)
print(type(szöveg))
print(logikai_érték)
print(type(logikai_érték))

magas = True
barna_hajú = False
szemüveges = True

if magas and barna_hajú:
    print("magas barna")

if magas or barna_hajú:
    print("vagy magas vagy barna")

if not barna_hajú:
    print("Biztos szőke!")





