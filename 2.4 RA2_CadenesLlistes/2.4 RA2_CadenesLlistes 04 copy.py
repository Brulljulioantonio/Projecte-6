# Què fa el programa: Demana una paraula i verifica si és un palíndrom (ex: "anna", "civic", etc.).
# Autor: Biel Rull Simon
# Data: 22/10/2025

# Versió 1.0

paraula = input("Introdueix una cadena de caràcters: ")
if paraula == paraula[::-1]:
    print("La paraula és un palíndrom.")
else:
    print("La paraula no és un palíndrom.")