# Què fa el programa: Escriu una funció filtra_parells(llista) que:
# Rebi una llista de nombres.
# Retorni una nova llista només amb els nombres parells.

# Autor: Biel Rull Simon

llista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filtra_parells(llista):
    for nombre in llista:
        if nombre % 2 != 0:
            llista.remove(nombre)
    return llista
# Descomentar seguent linea per provar la funció amb la llista definida
# print(filtra_parells(llista))

print(filtra_parells([1, 2, 3, 4, 5, 6]))
print(filtra_parells([10, 15, 20, 25, 30]))