import random
import numpy as np
import matplotlib.pyplot as plt
import time
from sympy import isprime    #pip install sympy    

# yield kulcsszó
# Felsoroló függvény
def négyzet_számok():
    i = 1
    while True:
        yield i**2 # Visszaadja i négyzetét (nem állítja le a függvényt)
        i += 1
        
for num in négyzet_számok():
    if num > 100:
        break # kilép a ciklusból
    print(num)
    
#for num in négyzet_számok():
#    print(num)
    
def myRange(upperBound):
    i = 0
    while i < upperBound:
        yield i
        i += 1
        
for i in myRange(10):
    print(i, end = " ")
print()

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
def fib_generator(from_num, to_num):
    a = 1
    b = 1
    for i in range(to_num):
        if i >= from_num-1:
            yield a
        a, b = b, a + b
        if i >= to_num:
            break

for i in fib_generator(0, 15):
    print(i, end= " ")
print()

def yield_evens(lista):
    for item in lista:
        if item % 2 == 0:
            yield item

for i in yield_evens([1,2,3,4,5,6,1,2,4,6,7,2,3,6,9,5,2,1,4,1]):
    print(i, end=" ")
print()

def filter_list(lista, func):
    for item in lista:
        if func(item):
            yield item    

def is_even(num):
    return num % 2 == 0

def is_two_digit(num):
    return num >= 10 and num <= 99

lista = [1, 9, 2, 6,34,7,5,3,2,4,123,7,4,3,2,3,51,8,9,4,324,12,2,23,4,35]
evens = [i for i in filter_list(lista, is_even)]
two_digits = [i for i in filter_list(lista, is_two_digit)]
primes = [i for i in filter_list(lista, isprime)]

print(lista)
print(evens)
print(two_digits)
print(primes)

# Kő papír olló

def rock_paper_scirrors():
    #player_choice = int(input("Kő (1), Papír (2), Olló (3). Válassz!\n"))
    player_choice = random.randint(1,3)
    comp_choice = random.randint(1,3)
    winner = 0 # 0 - döntetlen, 1 - player nyert, -1 - szg. nyert
    if player_choice == 1 and comp_choice == 3 or player_choice == 2 and comp_choice == 1 or player_choice == 3 and comp_choice == 2:
        winner = 1
    elif player_choice == comp_choice:
        winner = 0
    else:
        winner = -1
    return winner

wins = 0
losses = 0
ties = 0
for i in range(100):
    result = rock_paper_scirrors()
    if result == 1:
        wins += 1
        print("Nyertél!")
    elif result == 0:
        ties += 1
        print("Döntetlen!")
    else:
        losses += 1
        print("Vesztettél!")
print(f"Győzelmek: {wins}\nDöntetlenek: {ties}\nVereségek: {losses}")

def show_results_barchart():
    labels = ["Győzelmek", "Vereségek", "Döntetlenek"]
    y_pos = np.arange(len(labels)) # [0, 1, 2]
    plt.bar(y_pos, [wins, losses, ties], align = "center")
    plt.xticks(y_pos, labels = labels)
    plt.title("100 Kő-Papír-Olló játék eredménye")
    plt.xlabel("Kimenetel")
    plt.ylabel("Előfordulás")
    plt.savefig(f"4ora_kepek/results_{time.time()}.png")
    
show_results_barchart()

str(time.strftime("%Y%m%d_%H%M%S"))