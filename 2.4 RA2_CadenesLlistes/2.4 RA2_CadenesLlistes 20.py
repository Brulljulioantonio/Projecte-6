# Què fa el programa: Demana una llista de paraules i crea una nova llista amb només les paraules que comencen per vocal.
# Autor: Biel Rull Simon
# Data: 22/10/2025

# Versió 1.0

llista = input("Introdueix una llista de paraules separades per espais: ").split()
vocals = 'aeiouAEIOU'
paraules_vocal = []
for i in llista:
    if i[0] in vocals:
        paraules_vocal.append(i)
print(paraules_vocal)