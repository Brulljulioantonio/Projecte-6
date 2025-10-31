# Què fa el programa: Escriu una funció que sumi tots els nombres d'una llista.
# Autor: Biel Rull Simon
# Data: 22/10/2025

# Versió 1.0

llista_nombres = list(input("Introdueix una llista de nombres separats per espais: ").split())
suma = 0
for nombre in llista_nombres:
    suma += int(nombre)
print("La suma dels nombres és:", suma)