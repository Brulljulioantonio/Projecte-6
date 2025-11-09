# Què fa el programa: Escriu una funció maxim(a, b, c) que retorni el nombre més gran entre els tres.
# Autor: Biel Rull Simon

# Descomentar linies 5,6,7 i 12 per provar amb valors introduïts per l'usuari
# a = int(input("introdueix el valor nº1 "))
# b = int(input("introdueix el valor nº2 "))
# c = int(input("introdueix el valor nº3 "))

def maxim(a, b, c):
    n_max = max(a, b, c)
    return n_max
# print(maxim(a, b, c))

print(maxim(3, 7, 5))
print(maxim(10, 2, 8))
print(maxim(1, 1, 1))