# Què fa el programa: Aquest programa demana a l'usuari que introdueixi un número enter positiu i després imprimeix una sèrie de números des de 1 fins al número introduït, sumant-hi el mateix número a cada iteració.
# Autor: Biel Rull Simon
# Data: 17/10/2025

# Versió 1.0

try:
    num = int(input("Introdueix un número enter positiu: "))
    for i in range(1, 11):
        print(num, "*" ,i, "=", num * i)

except ValueError:
    print("Si us plau, introdueix un número enter vàlid.")