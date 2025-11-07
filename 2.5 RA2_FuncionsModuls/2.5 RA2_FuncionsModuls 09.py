# Què fa el programa: Escriu una funció estat_persona(edat) que:
# 1. Retorni "Menor d'edat", "Adult" o "Jubilat" segons l'edat.
# 2. Torni tant l'estat com una descripció (return estat, descripcio).

# Autor: Biel Rull Simon
edat = int(input("Introdueix una edat "))

def estat_persona(edat):
    if edat < 18:
        return "menor d'edat"
    elif edat < 64:
        return "major d'edat"
    elif edat >= 65:
        return "jubilat"
        
print(estat_persona(edat))