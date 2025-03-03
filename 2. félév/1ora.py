# Függvények visszatérési érték nélkül
def say_hi():
    print("Szia!")

def say_hi_to(name):
    print(f"Szia {name}!")

def say_time_hi_to(napszak, name):
    if napszak == 1:
        print(f"Jó reggelt {name}!")
    elif napszak == 2:
        print(f"Jó napot {name}!")
    elif napszak == 3:
        print(f"Jó napot {name}!")
    elif napszak == 4:
        print(f"Jó estét {name}!")
    else:
        print(f"Szia {name}!")

# Függvények visszatérési értékkel

szöveg = say_hi()
print(szöveg) #None

def get_animal():
    return "cica" # Visszatérési érték: "cica"

szöveg = get_animal()
print(szöveg) #cica

def get_color():
    print("get_color() függvény meghívva.")
    return "piros" # Ha a függvény return-höz ér, akkor befejezi a futását
    print("get_color() befejezte a futását.") # Ez a rész nem fut le

print(get_color())

def abs(num):
    if num < 0:
        return num * -1
    return num

print(abs(5))
print(abs(-5))

def f(x): # x az f függvény paramétere
    return 3*x - 4

print(f(1)) # 1 az f függvény argumentuma (argument)
print(f(2))
print(f(3))
print(f(4))

#Definíciókor (létrehozás) a zárójelbe írt értékek neve: paraméter
#Függvény híváskor a zárójelbe írt értékek neve: argumentum

def add(a, b):
    return a + b

print(add(3, 4)) #7
print(add(1, add(3,4))) #8