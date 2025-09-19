# Què fa el programa:
# Autor: Biel Rull Simon
# Data: 19/09/25

# Versió 1.0

# Especificacions d'entrada

import math

PI = 3.1416 # Constant

def calcular_area(radi): # Funció
    return PI * radi ** 2

radi = float(input("Introdueix el radi: ")) # Variable que llegeix input de l'usuari
area = calcular_area(radi) # Variable
print("L'àrea del cercle és:", area) # Resultat