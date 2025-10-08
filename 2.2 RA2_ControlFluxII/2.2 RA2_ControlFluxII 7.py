# Què fa el programa: 
# Autor: Biel Rull Simon
# Data: 

# Versió 1.0

texto = input("Text a invertir: ")
invertido = ""
i = len(texto) - 1

while i >= 0:
    invertido += texto[i]
    i -= 1

print("Texto invertit:", invertido)