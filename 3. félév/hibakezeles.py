# Olvassunk be két egész számot és írjuk ki a hányadosukat
def division(a,b):
    try:
        a = int(input("Add meg az első egész számot: "))
        b = int(input("Add meg a második egész számot: "))
        print(f"{a} / {b} = {a / b}")
    except ValueError:
        print("Egész számot kell megadni!")
    except ZeroDivisionError:
        print("0-val nem szabad osztani!")
    except Exception as ex:
        # Except ágba akkor lépünk ha a try blokkban hiba lépett felű
        print(type(ex)) # ValueError, TypeError, SyntaxError, stb.
        print("Valami hiba történt")
    finally:
        # Ez lefut akkor is ha volt hiba és akkor is ha nem
        print("Program vége.")

class EmptyStringError(Exception):
    def __init__(self, message = "The str object is empty."):
        super().__init__(message) # super() = származtatott osztály (Exception)

class NotFullNameError(Exception):
    def __init__(self, message = "The str object has no space characters."):
        super().__init__(message)

def name_splitter(name: str) -> list[str]:
    if name == "":
        raise EmptyStringError()
    if " " not in name:
        raise NotFullNameError()
    return name.split(" ")

print(name_splitter("Kis Pista"))
print(name_splitter("Kis Pista János"))

try:
    name = input("Adj meg egy teljes nevet: ")
    print(name_splitter(name))
except EmptyStringError:
    print("Figyelj rá, hogy ne üres szöveget adj meg!")
except NotFullNameError:
    print("Az illető teljes nevét add meg kérlek!")
except Exception as ex:
    print(type(ex))
