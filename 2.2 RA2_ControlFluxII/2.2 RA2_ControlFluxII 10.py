# Què fa el programa: preguntar un nombre per fer un patró d'asteriscs
# Autor: Biel Rull Simon
# Data:  8/10/25

# Versió 1.0

count = int(input("quants cicles? "))
restacicle = 1
patro = "*"
sumpatro = "*"

while count != 0:
    print(patro)
    patro = patro + sumpatro
    count = count - restacicle