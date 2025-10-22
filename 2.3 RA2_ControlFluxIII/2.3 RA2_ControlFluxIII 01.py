# Què fa el programa: Aquest programa demana a l'usuari que introdueixi un número enter positiu i després imprimeix una sèrie de números des de 0 fins al número introduït, incloent-lo.
# Autor: Biel Rull Simon
# Data: 17/10/2025

# Versió 1.0

try:
    num = int(input("Introdueix un número enter positiu per fer el compte enrere: "))
    num = num + 1
    for i in range(0, num):
        print(i)
except Exception:
    print("Si us plau, introdueix un número enter positiu vàlid.")