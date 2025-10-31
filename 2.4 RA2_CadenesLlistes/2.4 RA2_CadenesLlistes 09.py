# Què fa el programa: Crea un programa que divideixi una frase en paraules i les mostri una per una.
# Autor: Biel Rull Simon
# Data: 22/10/2025

# Versió 1.0

frase = input("Introdueix una frase: ")
paraules = frase.split()
for paraula in paraules:
    print(paraula)