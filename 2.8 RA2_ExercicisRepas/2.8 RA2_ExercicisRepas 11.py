# Què fa el programa:
# Autor: Biel Rull Simon

num = list(map(int, input("Introdueix un llistat de numeros: ").split()))
max = 0

for i in num:
    if i > max:
        max = i
print(max)