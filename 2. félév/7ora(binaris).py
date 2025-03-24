# A kettes számrendszer használata (16-os számrendszer)
binary = bin(64) # 0b100000    (0b jelzi hogy 2-es számrendszer)
print(binary)
print(type(binary)) # <class 'str'>

# Ha le akarjuk szedni a 0b-t az elejéről:
print(binary[2:]) # Az első két karakterér a stringnek leszedjük

hexa = hex(5643258) # 16-os számrendszerbe konvertál (ugyanúgy stringként menti)
print(hexa)         # 0x561bfa         A 0x jelöli a 16-os számrendszert,
print(type(hexa))   # <class 'str'>


# Ha le akarjuk szedni a 0x-t az elejéről:
print(hexa[2:]) # Az első két karakterér a stringnek leszedjük

# Hol használjuk a 16-os számrendszert?
# RGB kódok (színeknél) #FF1010  255 piros 16 zöld 16 kék (Főként piros színt kapunk)
# MAC címeknél (A számítógépünk fizikai címe)   pl.: 98-2C-BC-48-66-C4
# IPv6 ip címek: fe80::edfd:4be4:f9e8:55a%5

class Valami:
    def __init__(self):
        pass
    
var = Valami()
print(var)          # <__main__.Valami object at 0x000001B515BEDB10> Memóriacímét


# Kettes számrendszerből 10-esbe konvertálás

binary = "1011101101"
num = int(binary) # Alapesetben az int() fgv. 10-es számrendszerű számként értelmezi
print(num) # 1011101101
num = int(binary, 2)
print(num) # 749

hexa = "4F1EAC"
num = int(hexa, 16)
print(num) # 5185196
