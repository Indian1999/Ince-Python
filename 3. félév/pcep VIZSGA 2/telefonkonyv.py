telefonkonyv = {"Segélyhívó": "112",
                "Mentők": "104",
                "Rendőrség": "105",
                "Tűzoltóság": "107"
                }

def new_contact():
    nev = input("Név: ")
    telefonszam = input("Telefonszám: ")
    telefonkonyv[nev] = telefonszam
    print("Kontakt hozzáadva!")

def search_contact():
    nev = input("Keresett kontakt: ")
    if nev in telefonkonyv.keys():
        print("Telefonszám:", telefonkonyv[nev])
    else:
        print("Nem szerepel ez a kontakt a telefonkönyben!")

def delete_contact():
    nev = input("Keresett kontakt: ")
    if nev in telefonkonyv.keys():
        del telefonkonyv[nev]
        print("Kontakt törölve!")
    else:
        print("Nem szerepel ez a kontakt a telefonkönyben!")

def list_contacts():
    for nev, telefonszam in telefonkonyv.items():
        print(f"{nev}: {telefonszam}")

def print_menu():
    print("Lehetőségek:")
    print("1. Új kontakt hozzáadása")
    print("2. Kontakt keresése név alapján")
    print("3. Kontakt törlése")
    print("4. Összes kontakt listázása")
    print("5. Kilépés")

while True:
    print_menu()
    valasztas = input("Valasztas: ")
    if valasztas == "1":
        new_contact()
    elif valasztas == "2":
        search_contact()
    elif valasztas == "3":
        delete_contact()
    elif valasztas == "4":
        list_contacts()
    elif valasztas == "5":
        break
    else:
        print("Érvénytelen menüpont!")
