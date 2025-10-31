# Què fa el programa: Crea una llista amb 5 nombres i imprimeix el major i el menor.
# Autor: Biel Rull Simon
# Data: 22/10/2025

# Versió 1.0

nombres = input("Introdueix 5 nombres separats per espais: ").split()
major = max(nombres)
menor = min(nombres)
print("El nombre major és:", major)
print("El nombre menor és:", menor)