jelszo = input("Add meg a jelszavad: ")

if len(jelszo) >= 8:
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    for char in jelszo:
        if char.islower():
            has_lower = True
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_digit = True
        if char in "!@#$%ˆ&*":
            has_special = True
    if not has_lower:
        print("A jelszóban szerepelnie kell legalább 1 kisbetűs karakternek!")
    elif not has_upper:
        print("A jelszóban szerepelnie kell legalább 1 nagybetűs karakternek!")
    elif not has_digit:
        print("A jelszóban szerepelnie kell legalább 1 számjegy karakternek!")
    elif not has_special:
        print("A jelszóban szerepelnie kell legalább 1 különleges karakternek!")
    else:
        print("A jelszó elég erős!")
else:
    print("A jelszónak minimum 8 karakter hosszúnak kell lennie!")