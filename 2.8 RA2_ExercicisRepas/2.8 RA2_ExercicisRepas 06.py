# Què fa el programa:
# Autor: Biel Rull Simon

try:

    num = int(input("Introdueix un numero: "))
    resultat = 0

    for i in range(1, num + 1):
        resultat = resultat + i
    print(resultat)

except ValueError:
    print("Valor no valid")