# Què fa el programa: Diu si un número es negatiu, positiu o zero
# Autor: Biel Rull Simon
# Data: 23/09/25

# Versió 1.0

def gracies(): # Definim la funció gracies
    print("Gràcies")

número = float(input("Número? ")) # L'usuari diu un número


if número > 0: # si es més gram que 0 es positiu
    print("És positiu")
    gracies() # Crida la funció gracies

elif número < 0: # si es menor que 0 es negatiu
    print("És negatiu")
    gracies() # Crida la funció gracies

elif número == 0: # si es igual a 0 es 0
    print("És zero")
    gracies() # Crida la funció gracies