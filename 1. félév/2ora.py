"""
name = "Logi Robert"
age = 10
gender = "robot"
height = 110
weight = 43.6
married = False # Not married / Married

print("Name: " + name)              #szöveg (string  (str))
print("Age: " + str(age))           #egész szám (integer (int))
print("Gender: " + gender)          #szöveg (string (str))
print("Height: " + str(height))     #egész szám (integer (int))
print("Weight: " + str(weight))     #lebegőpontos szám (float)
if married:                         #logikai érték (boolean (bool))
    print("Married")
else:
    print("Isn't married")

vacations = ["Madrid", "Paris", "München", "Las Vegas"] #Lista (list)
print("Visited cities: " + str(vacations))

location = input("Where is LogiRobi right now?\n")
vacations.append(location)
print("Visited cities: " + str(vacations))


lista = [4, 5, "cica", "kutya", True, False, True, 4, 4.56, [1,2,3]]
print(lista)
print(lista[3])
print("The list has this many elements:", len(lista))

for i in range(5): #range(5) = [0,1,2,3,4]
    print(i)

for i in range(len(lista)): # [0,1,2,3,...,9] ha a len(lista) = 10
    print(lista[i])
"""

numbers = [5, 9, 4, 0, 2, -6, -9, 8, -2, 8, 3, 1, 4, -4, 0, 2, 3]
print(numbers)

summa = 0
for i in range(len(numbers)):
    summa += numbers[i]
print("The sum of the elements:", summa)
print("The sum of the elements:", sum(numbers))
print(12 in numbers)
print("The largest number is:", max(numbers))
print("The smallest number is:", min(numbers))

index = 0
while index < len(numbers):
    print("cica" * index)
    index += 3


lista = []
szöveg = "quit"
while szöveg != "quit":
    szöveg = input("Write something here:\n")
    lista.append(szöveg)
print("You wrote these things:", lista)

a = int(input("Enter integer nr. 1:\n"))
b = int(input("Enter integer nr. 2:\n"))
c = a + b
print(str(a) + " + " + str(b) + " = " + str(c))

#Írjuk ki, hogy melyik szám a nagyobb

if a > b:
    print("The first number is the bigger!")
elif b > a:
    print("The second number is the bigger!")
else:
    print("The numbers are equal!")



