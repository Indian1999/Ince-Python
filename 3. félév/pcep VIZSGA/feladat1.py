a = int(input("Adj meg egy egész számot: "))
b = int(input("Még egy egész számot: "))
c = float(input("Adj meg egy lebegőpontos számot: "))

print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} % {b} = {a%b}")

print(f"{c} négyzetgyöke: {round(c**0.5 ,2)}")