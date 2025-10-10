# Què fa el programa: 
# Autor: Biel Rull Simon
# Data: 

# Versió 1.0

paraula = input("Introdueix una paraula: ")

vocals = "aeiouAEIOU"

contador = 0

for i in paraula:
    if i in vocals:
        contador += 1

print("La paraula conté" , contador , "vocals")