# Què fa el programa: Aquest programa demana a l'usuari que introdueixi un número enter positiu i després imprimeix una sèrie de números des de 2 fins al número introduït.
# Autor: Biel Rull Simon
# Data: 17/10/2025

# Versió 1.0

try:
    num = int(input("Introdueix un número primer: "))
    for i in range(2, num + 1):
        print(i)

except ValueError:
    print("Si us plau, introdueix un número enter vàlid.")