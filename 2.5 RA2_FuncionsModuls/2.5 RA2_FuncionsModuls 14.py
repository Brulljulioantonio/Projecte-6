# Què fa el programa: Aquest programa simula el llançament d'un dau de sis cares un nombre 'n' de vegades i calcula la mitjana dels resultats obtinguts.
# Autor: Biel Rull Simon

import random
def llança_dau(n):
    suma = 0
    for _ in range(n):
        tirada = random.randint(1, 6)
        suma += tirada
    mitjana = suma / n
    return mitjana
print(llança_dau(10))