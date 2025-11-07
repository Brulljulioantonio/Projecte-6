# Què fa el programa: Escriu una funció multiplica_tot(*nombres) que rebi qualsevol quantitat de nombres i retorni la seva multiplicació.
# Autor: Biel Rull Simon

nombres = input("introdueix varios nombres ").split()

def multiplica_tot(nombres):
    resultat = 1
    for i in nombres:
        resultat *= float(i)
    return resultat
print(multiplica_tot(nombres))