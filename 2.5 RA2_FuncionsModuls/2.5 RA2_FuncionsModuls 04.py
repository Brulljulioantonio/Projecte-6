# Què fa el programa: Escriu una funció es_parell(numero) que retorni True si numero és parell i False si no.
# Autor: Biel Rull Simon

numero = [1, 2, 3, 4, 5, 6]

def es_parell(numero):
    for i in numero:
        if i % 2 == 0:
            print("El número ", i ," és parell: " , True)
        else:
            print("El número ", i ," és parell: " , False)
es_parell(numero)