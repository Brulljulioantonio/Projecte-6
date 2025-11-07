# Què fa el programa: Escriu una funció es_parell(numero) que retorni True si numero és parell i False si no.
# Autor: Biel Rull Simon

numero = int(input("Introdueix un nombre enter: "))

def es_parell(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
print(es_parell(numero))