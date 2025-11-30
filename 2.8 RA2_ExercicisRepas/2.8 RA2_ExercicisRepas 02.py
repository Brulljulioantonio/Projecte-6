# Què fa el programa:
# Autor: Biel Rull Simon

try:

    num1 = int(input("Introdueix el valor 1: "))
    num2 = int(input("Introdueix el valor 2: "))
    num3 = int(input("Introdueix el valor 3: "))


    if num1 > num2 and num1 > num3:
        print("El valor 1 (",num1,") És mes gran")
    elif num2 > num1 and num2 > num3:
        print("El valor 2 (",num2,") És mes gran")
    elif num3 > num1 and num3 > num2:
        print("El valor 3 (",num3,") És mes gran")
    elif num1 == num2 and num1 == num3:
        print("Són iguals")

except ValueError:
    print("Valor no valid")