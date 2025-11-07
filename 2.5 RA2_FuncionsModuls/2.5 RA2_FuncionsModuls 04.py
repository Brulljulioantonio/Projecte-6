# Què fa el programa: Escriu una funció es_parell(numero) que retorni True si numero és parell i False si no.
# Autor: Biel Rull Simon

numero = [1, 2, 3, 4, 5, 6]

def es_parell(numero):
    parells = []
    for i in numero:
        if i % 2 == 0:
            return parells.append(True)
        else:
            return parells.append(False)
print(es_parell(numero))