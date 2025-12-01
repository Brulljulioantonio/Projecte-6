# Què fa el programa:
# Autor: Biel Rull Simon

frase = input("Introdueix una frase: ")
VOCAL = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
contador = 0

for i in frase:
    if i in VOCAL:
        contador = contador + 1
print("Dins de la frase/paraula hi havien", contador , "vocals")