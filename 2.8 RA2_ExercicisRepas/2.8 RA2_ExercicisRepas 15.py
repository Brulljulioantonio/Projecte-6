# Què fa el programa:
# Autor: Biel Rull Simon

try:

    num = (input("Introdueix un número decimal: "))
    print(int(num))
    
except ValueError:
    print("Valor no valid")