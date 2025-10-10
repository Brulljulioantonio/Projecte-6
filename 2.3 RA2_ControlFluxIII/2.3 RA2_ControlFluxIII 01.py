# Què fa el programa: Aquest programa demana a l'usuari un número i realitza un compte enrere des d'aquest número fins a zero.
# Autor: Biel Rull Simon
# Data: 10/10/2025

# Versió 1.0

# Especificacions d'entrada
num = -1
while num <= 0:
    num = int(input("Introdueix un número per fer el compte enrere: "))
for i in range(num, -1, -1):
    print(i)