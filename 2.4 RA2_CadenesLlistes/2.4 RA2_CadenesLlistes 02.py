# Què fa el programa: Demana una frase i compta quantes vocals conté.
# Autor: Biel Rull Simon
# Data: 22/10/2025

# Versió 1.0

text = input("Introdueix una cadena de caràcters: ")
vocals = "aeiouAEIOU"
comptador = 0
for i in text:
    if i in vocals:
        comptador += 1
print(comptador)