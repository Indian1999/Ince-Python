#1. feladat: Melyik síknegyedben található a pont?
"""
4|1
---
3|2
"""
#x = int(input("Add meg az x koordinátát!\n"))
#y = int(input("Add meg az y koordinátát!\n"))
x = 0
y = 0
#(x;y) (2;3)
if x > 0 and y > 0:
    print("1. síknegyed")
if x > 0 and y < 0:
    print("2. síknegyed")
if x < 0 and y < 0:
    print("3. síknegyed")
if x < 0 and y > 0:
    print("4. síknegyed")

if x == 0 and y == 0:
    print("origó")
elif x == 0:
    print("y tengely")
elif y == 0:
    print("x tengely")


#2. feladat: Bontsunk fel egy számot prímtényezőkre

num = int(input("Adj meg egy egész számot!\n"))
primtenyezok = []
while num > 1:
    for i in range(2, num + 1):
        if num % i == 0:
            num //= i
            primtenyezok.append(i)
            break
print(primtenyezok)

#3. feladat: találjuk meg két szám legnagyobb közös osztóját:
a = int(input("Add meg az első számot!\n"))
b = int(input("Add meg a második számot!\n"))

kisebb = a
if b < a:
    kisebb = b
lnko = 1
for i in range(2, kisebb + 1):
    if a % i == 0 and b % i == 0:
        lnko = i
print("lnko =", lnko)

#4. feladat: adjuk meg két szám legkisebb közös töbszörösét
nagyobb = a
if b > a:
    nagyobb = b

i = nagyobb
while not (i % a == 0 and i % b == 0):
    i += 1
print("lkkt =", i)

#5. feladat: Oldjunk meg egy másodfokú egyenletet
a = int(input("Add meg az x^2 előtt álló számot!\n"))
b = int(input("Add meg az x előtt számot!\n"))
c = int(input("Add meg az x nélküli számot!\n"))

diszkrimáns = b**2 - 4 * a * c
if diszkrimáns < 0:
    print("Nincs megoldás!")
elif diszkrimáns == 0:
    print("x =", -b / (2*a))
else:
    x1 = (-b + diszkrimáns**(1/2)) / (2*a)
    x2 = (-b - diszkrimáns**(1/2)) / (2*a)
    print("x1 =", x1)
    print("x2 =", x2)


#6. feladat: Bináris számok