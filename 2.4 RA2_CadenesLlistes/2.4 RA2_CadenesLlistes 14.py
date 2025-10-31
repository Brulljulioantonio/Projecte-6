# Què fa el programa: Demana 10 números i crea dues llistes: una amb els parells i una altra amb els senars.
# Autor: Biel Rull Simon
# Data: 22/10/2025

# Versió 1.0

parells = []
senars = []
num = list(map(int, input("Introdueix números separats per espais: ").split()))
for i in num:
    if i % 2 == 0:
        parells.append(i)
    else:
        senars.append(i)
print("Llista de nombres parells:", parells)
print("Llista de nombres senars:", senars)