# Què fa el programa: Write a program that, given a number of seconds n, prints the number of hours, minutes and seconds represented by n.
# Autor: Biel Rull Simon

n = int(input("Introdueix un nombre de segons: "))
hores = n // 3600
n = n % 3600
minuts = n // 60
segons = n % 60
print(hores, "hores,", minuts, "minuts i", segons, "segons")