# Què fa el programa:
# Autor: Biel Rull Simon

try:
    contador = int(input("Numero de repeticions: "))
    while contador != 0 and contador > 0:
        print("Hola!")
        contador = contador - 1

except ValueError:
    print("Valor no valid")