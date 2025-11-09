# Què fa el programa: Escriu una funció estat_persona(edat) que:
# 1. Retorni "Menor d'edat", "Adult" o "Jubilat" segons l'edat.
# 2. Torni tant l'estat com una descripció (return estat, descripcio).

# Autor: Biel Rull Simon

# Cambiar linea 8 per la 9 per provar inputs de l'usuari
# edat = list(map(int, input("Introdueix una edat ").split()))
edat = [12, 25, 70]

def estat_persona(edat):
    resultats = []
    for i in edat:
        if i < 18:
            resultats.append("menor d'edat")
        elif i < 64:
            resultats.append("major d'edat")
        else:
            resultats.append("jubilat")
    return resultats

for i in estat_persona(edat):
    print(i)