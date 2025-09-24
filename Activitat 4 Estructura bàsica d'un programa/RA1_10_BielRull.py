# Què fa el programa: Calcula la suma, resta, divisió i multiplicació dels valor introduïts
# Autor: Biel Rull Simon
# Data: 23/09/25

# Versió 1.0

import os # importem comandes del sistema

os.system("cls") # fem un clear screen

n1 = float(input("Número 1: ")) # demanem numero 1
n2 = float(input("Número 2: ")) # demanem numero 2

os.system("cls") # fem un clear screen

# fiquem cada operacio amb els numeros de avans
print("Suma:",n1 + n2)
print("Resta:",n1 - n2)
print("Multiplicació:",n1 * n2)
print("Divisió:",n1 / n2)