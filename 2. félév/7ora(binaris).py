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
# MAC címeknél (A számítógépünk fizikai címe)   
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

hatos = "421210"
num = int(hatos, 6)
print(num) # 33990

# 16-osból 2-esbe váltsunk át
# először 16ból 10-be, utána 10-ből 2-be
hexa = "3F5A"
binary = bin(int(hexa,16))
print(binary) # 0b11111101011010


# Bináris operátorok (&, |, ^, <<, >>)

num1 = 42 # 0101010
num2 = 97 # 1100001

print(num1 & num2) # 32
print(num1 | num2) # 107
print(num1 ^ num2) # 75                       # alt gr + 3 (kétszer)

num1 = 13 # 1101  (8 + 4 + 1)
num2 = 7  # 0111  (4 + 2 + 1)

print(num1 & num2) # 0101 -> 4 + 1 = 5
print(num1 | num2) # 1111 -> 8 + 4 + 2 + 1 = 15
print(num1 ^ num2) # 1010 -> 8 + 2 = 10

# Jobbra/Balra shiftelés (<<, >>)

num = 42

print(num >> 1) # 21
print(num >> 2) # 10
print(num >> 3) # 5

# Tapasztalat: Jobbra shiftelésnél 2-vel osztunk (maradék nélkül)
# 1-el megyünk jobbra (2-vel osztunk) (2^1)
# 2-vel megyünk jobbra (4-el) (2^2)
# 3-al megyünk jobbra (8-al osztunk)(2^3)

print(num << 1) # 84
print(num << 2) # 168
print(num << 3) # 336

# Itt pedig mindig 2-vel szorzunk


# feladat: Határozzuk meg, hogy x GigaByte, hány TeraByte, MegaByte és hány Byte?
# 1 TB = 1024 GB
# 1 GB = 1024 MB
# 1 MB = 1024 B
# 1  B = 8 bit      ( 1 bit egy 0-s vagy 1-s)

giga = int(input("Add meg a GigaByte-ok számát!\n"))
print(f"{giga} GB = {giga >> 10} TB")
print(f"{giga} GB = {giga << 10} MB")
print(f"{giga} GB = {giga << 20} Byte")
print(f"{giga} GB = {giga << 23} bit")


# IP címek:
# IPv4 Address    : 192.168.44.135
# Subnet Mask     : 255.255.255.0 # Ebből lehet kiszámolni a hálózatnak az IP-címét
# Default Gateway : 192.168.44.1
# Hálózat IP címe : 192.168.44.0

# Ha az IP címünket összeéseljük a Hálózati mask, akkor megkapjuk a hálózat IP-címét
ipQ1 = 192
ipQ2 = 168
ipQ3 = 44
ipQ4 = 135
maskQ1 = 255
maskQ2 = 255
maskQ3 = 255
maskQ4 = 192
print(f"Az IP címed: {ipQ1}.{ipQ2}.{ipQ3}.{ipQ4}")
print(f"A hálózati maszk: {maskQ1}.{maskQ2}.{maskQ3}.{maskQ4}")
print(f"A hálózat IP címe: {ipQ1 & maskQ1}.{ipQ2 & maskQ2}.{ipQ3 & maskQ3}.{ipQ4 & maskQ4}")
print(f"Összevagyolva: {ipQ1 | maskQ1}.{ipQ2 | maskQ2}.{ipQ3 | maskQ3}.{ipQ4 | maskQ4}")
print(f"Össze-kizáróvagyolva: {ipQ1 ^ maskQ1}.{ipQ2 ^ maskQ2}.{ipQ3 ^ maskQ3}.{ipQ4 ^ maskQ4}")
