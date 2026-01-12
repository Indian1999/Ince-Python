# a feladat:
for i in range(1, 6):
    print("*" * i)

# b feladat:
i = 5
while i > 0:
    print("*" * i)
    i -= 1

# c feladat:
print("3-mal és 5-tel osztható számok:")
for i in range(1, 101):
    if i % 3 != 0: # Nem osztható 3-mal
        continue
    if i % 5 != 0:
        continue
    print(i, end= " ")
print()

# d feladat:
a = 0
b = 1
print("A fibonacci sorozat első 10 eleme: 0 1 ", end = "")
for i in range(8):
    a, b = b, a + b
    print(b, end= " ")
print()
