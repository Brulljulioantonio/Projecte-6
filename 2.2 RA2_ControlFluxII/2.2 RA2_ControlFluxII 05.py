# Què fa el programa: demana un numero enter i diu si és parell o senar
# Autor: Biel Rull Simon
# Data:  8/10/25

# Versió 1.0

num = int(input("Numero enter? "))

while num < 0:
    num = int(input("Numero enter? "))

if num % 2 == 0:
    print("Parell")

elif num % 2 != 0:
    print("Senar")