# Què fa el programa: Escriu una funció maxim(a, b, c) que retorni el nombre més gran entre els tres.
# Autor: Biel Rull Simon

a = int(input("introdueix el valor nº1 "))
b = int(input("introdueix el valor nº2 "))
c = int(input("introdueix el valor nº3 "))

def maxim(a, b, c):
    n_max = max(a, b, c)
    return n_max
print(maxim(a, b, c))