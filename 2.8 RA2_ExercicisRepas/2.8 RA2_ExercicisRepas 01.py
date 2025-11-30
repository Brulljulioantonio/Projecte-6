# Què fa el programa:
# Autor: Biel Rull Simon

try:
    num = int(input("Introdueix un número enter "))
    if num % 2 == 0:
        print(num, "És parell")
    elif num % 2 != 0:
        print(num, "És senar")
except ValueError:
    print("Valor no valid")