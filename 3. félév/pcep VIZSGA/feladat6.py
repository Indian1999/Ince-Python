def faktorialis(num):
    if num == 0:
        return 1
    return num * faktorialis(num - 1)

def prim_e(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def szamjegyek_osszege(num):
    összeg = 0
    for digit in str(num):
        összeg += int(digit)
    return összeg

def palindrom(string):
    return string == string[::-1]

print(faktorialis(5))
print(faktorialis(9))
print(prim_e(10))
print(prim_e(11))
print(szamjegyek_osszege(123))
print(szamjegyek_osszege(12323))
print(palindrom("kutya"))
print(palindrom("görög"))
    
