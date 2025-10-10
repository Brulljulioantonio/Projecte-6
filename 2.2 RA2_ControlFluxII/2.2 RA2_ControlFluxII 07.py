# Què fa el programa: mostra el text invertit
# Autor: Biel Rull Simon
# Data:  8/10/25

# Versió 1.0

texto = input("Text a invertir: ")
invertido = ""
i = len(texto) - 1

while i >= 0:
    invertido += texto[i]
    i -= 1

print("Texto invertit:", invertido)