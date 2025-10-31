# Què fa el programa: Demana una cadena i compta quantes vegades apareix una lletra concreta.
# Autor: Biel Rull Simon
# Data: 22/10/2025

# Versió 1.0

frase = input("Introdueix una frase: ")
lletra = input("Introdueix una lletra per comptar: ")
contador = 0
for i in frase:
    if i == lletra:
        contador += 1
print("la lletra", lletra, "apareix", contador, "vegades")