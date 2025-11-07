# Què fa el programa: Escriu una funció suma(a, b) que retorni la suma de a i b.
# Autor: Biel Rull Simon

a = int(input("Introdueix el primer nombre: "))
b = int(input("Introdueix el segon nombre: "))

def suma(a, b):
    resultat = a + b
    return resultat
print(suma(a, b))