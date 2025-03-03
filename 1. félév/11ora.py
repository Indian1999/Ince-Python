"""
# 1. feladat: Írjunk ki számokat háromszög alakban
for i in range(1, 11):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    
# 2. feladat: Írjuk ki a számokat 1300-tól 2100-ig amik oszthatók 7-tel és 4-gyel
for i in range(1300, 2101):
    if i % 7 == 0 and i % 4 == 0:
        print(i, end=" ")
print()
# 3. feladat: Írjuk ki az összes lehetséges név kombinciót
vezeték_nevek = ["Kovács", "Balogh", "Kerekes", "Horváth"]
kereszt_nevek = ["András", "Béla", "Cecil", "Dominik", "Elemér"]
for i in range(len(vezeték_nevek)):
    for j in range(len(kereszt_nevek)):
        print(vezeték_nevek[i] + " " + kereszt_nevek[j])

# 4. feladat: Találjuk meg az összes párt a listában
nevek = ["András", "Béla", "Cecil", "Dominik", "Elemér", "Ferenc", "Gábor", "Hugó"]
for i in range(len(nevek)):
    for j in range(len(nevek)):
        if i < j:
            print(nevek[i], nevek[j])

# 5. feladat: Találjuk meg egy adott szám prím osztóit
num = int(input("Adj meg egy pozitív egész számot!\n"))
primtenyezok = []
for i in range(2, num + 1):
    prime = True
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            prime = False
    if num % i == 0 and prime:
        primtenyezok.append(i)
    
print(primtenyezok)
# 6. feladat: Forgassunk el egy listát egy megadott értékkel
lista = [1,2,3,4,5,6] # ha 2 vel forgatunk balra -> [3,4,5,6,1,2]
# Ha 2-vel forgatjuk jobbra -> [5,6,1,2,3,4]
print(lista)
rotate = int(input("Mennyivel forgassam el a listát?\n"))
rotate = rotate % len(lista)
irány = input("Melyik irányba forgassam? (bal/jobb)\n")
if irány == "bal":
    lista = lista[rotate:] + lista[:rotate]
else:
    lista = lista[-rotate:] + lista[:-rotate]
print(lista)
"""
# Bonus feladatok: Turle
import turtle
turtle_screen = turtle.getscreen()
turtle_actor = turtle.Turtle()
"""
turtle_actor.color("red")
for i in range(3):
    turtle_actor.forward(100)
    turtle_actor.left(120)
turtle.exitonclick()
"""
"""
colors = ["red", "pink", "yellow", "green", "blue", "orange"]
for i in range(8, 2, -1):
    turtle_actor.color(colors[i-3])
    turtle_actor.fillcolor(colors[i-3])
    turtle_actor.begin_fill()
    for j in range(i):
        turtle_actor.forward(60)
        turtle_actor.left(360/i)
    turtle_actor.end_fill()
turtle.exitonclick()
"""
"""
turtle_actor.forward(100)
turtle_actor.backward(200)
turtle_actor.left(10)
turtle_actor.right(10)
turtle_actor.penup()
turtle_actor.goto(50, 50)
turtle_actor.pendown()
turtle_actor.setx(150)
turtle_actor.sety(10)
turtle_actor.begin_fill()
turtle_actor.end_fill()
"""
#Rajzoljunk egy magyar zászlót
turtle_screen.bgcolor("black")

turtle_actor.color("green")
turtle_actor.begin_fill()
turtle_actor.forward(200)
turtle_actor.left(90)
turtle_actor.forward(80)
turtle_actor.left(90)
turtle_actor.forward(200)
turtle_actor.left(90)
turtle_actor.forward(80)
turtle_actor.backward(80)
turtle_actor.left(90)
turtle_actor.end_fill()

turtle_actor.color("white")
turtle_actor.begin_fill()
turtle_actor.forward(200)
turtle_actor.left(90)
turtle_actor.forward(80)
turtle_actor.left(90)
turtle_actor.forward(200)
turtle_actor.left(90)
turtle_actor.forward(80)
turtle_actor.backward(80)
turtle_actor.left(90)
turtle_actor.end_fill()

turtle_actor.color("red")
turtle_actor.begin_fill()
turtle_actor.forward(200)
turtle_actor.left(90)
turtle_actor.forward(80)
turtle_actor.left(90)
turtle_actor.forward(200)
turtle_actor.left(90)
turtle_actor.forward(80)
turtle_actor.backward(80)
turtle_actor.left(90)
turtle_actor.end_fill()

turtle.exitonclick()





