# Què fa el programa: 
# Autor: Biel Rull Simon
# Data: 

# Versió 1.0

num = int(input("Numero enter? "))

while num < 0:
    num = int(input("Numero enter? "))

if num % 2 == 0:
    print("Par")

elif num % 2 != 0:
    print("Impar")