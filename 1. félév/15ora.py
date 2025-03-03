import random

class Warrior:
    #Konstruktór függvény:
    def __init__(self, hp, dmg, arm):
        self.health = hp
        self.damage = dmg
        self.armor = arm

    def __str__(self):
        return f"Health: {self.health} Damage: {self.damage} Armor: {self.armor}"
    
    def takeDamage(self, amount):
        self.health -= amount * (1 - self.armor/100)

    def healing(self, amount):
        self.health += amount

    def setArmor(self, value):
        self.armor = value


jack = Warrior(100, 10, 35) 
kevin = Warrior(100, 15, 10)
gameOn = True
turn_of_jack = True

while gameOn:
    print("Játékos:", jack)
    print("Ellenfél:", kevin)
    if turn_of_jack:
        jack.setArmor(35)
        print("Te következel!")
        action = input("Válassz egy akciót (1: támadás, 2: gyógyulás, 3: védekezés, 4: vérengzés)!\n")
        if action == "1":
            print("Megtámadtad az ellenfeledet!")
            kevin.takeDamage(jack.damage)
        elif action == "2":
            print("Megpihensz újratöltődni.")
            jack.healing(15)    
        elif action == "3":
            print("Felemeled a pajzsod extra védelemért.")
            jack.setArmor(jack.armor + 50)
        else:
            print("Vérengzően megtámadod az ellenfeled!")
            kevin.takeDamage(jack.damage*2)
            jack.setArmor(jack.armor - 100)

    else:
        kevin.setArmor(10)
        print("Az ellenfeled következik!")
        action = random.randint(1, 4)
        if action == 1:
            print("Az ellenfeled rádtámad!")
            jack.takeDamage(kevin.damage)
        elif action == 2:
            print("Az ellenfeled megálltt gyógyulni.")
            kevin.healing(15)
        elif action == 3:
            print("Az ellenfeled védekezik.")
            kevin.setArmor(kevin.armor + 50)
        else:
            print("Az ellenfeled vérengzően megtámad!")
            jack.takeDamage(kevin.damage*2)
            kevin.setArmor(kevin.armor - 100)

    turn_of_jack = not turn_of_jack
    if jack.health <= 0:
        print("Meghaltál! Talán legközelebb!")
        gameOn = False
    if kevin.health <= 0:
        print("Legyőzted az ellenfeled! Nyertél!")
        gameOn = False
