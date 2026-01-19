# 1. feladat: számológép (HF)

# 2. feladat:

penz = int(input("Add meg a kifizetendő összeget: "))

cimletek = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5]
felhasznalt = [0 for i in range(len(cimletek))] # [0,0,0, ...]

for cimlet in cimletek:
    print(f"{cimlet} Ft: {penz // cimlet} db")
    penz = penz % cimlet

# 3. feladat:

def tizedes_eltolas(num, x):
    num = list(str(num))
    tizedes_index = num.index(".")
    uj_index = tizedes_index + x
    ismetles = x if x > 0 else -x
    for i in range(ismetles):
        if uj_index < tizedes_index: # balra toljuk a tizedes vesszőt
            if tizedes_index >= 2:
                num[tizedes_index], num[tizedes_index-1] = num[tizedes_index-1], num[tizedes_index]
                tizedes_index -= 1
            else:
                num[tizedes_index], num[tizedes_index-1] = num[tizedes_index-1], num[tizedes_index]
                num.insert(0, "0")
        else: # jobbra
            if tizedes_index < len(num) - 1:
                num[tizedes_index], num[tizedes_index+1] = num[tizedes_index+1], num[tizedes_index]
                tizedes_index += 1
            else:
                num.insert(tizedes_index, "0")
                tizedes_index += 1
    if num[-1] == ".":
        num.append("0")
    return "".join(num) # "" elválasztó stringgel összefűzi a lista elemeit

mantissza = float(input("Add meg a mantisszát: "))
kitevő = int(input("Add meg a kitevőt: "))
print(f"Tényleges érték: {tizedes_eltolas(mantissza, kitevő)}")
print(f"Tudományos alak: {mantissza}e{kitevő}")
if mantissza > 0:
    print("Pozitív szám")
elif mantissza < 0:
    print("Negatív szám")
else:
    print("Nulla")
