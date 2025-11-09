# Què fa el programa: Fes servir-los des d’un altre fitxer per calcular coses com la força gravitatòria.
# Autor: Biel Rull Simon

import constants

massa = 10

def força_gravitòria(massa):
    return massa * constants.GRAVETAT
print(força_gravitòria(massa))