# Què fa el programa: Aquest programa demana a l'usuari que introdueixi una cadena de caràcters i després compta i imprimeix el nombre de vocals que conté la cadena.
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