llista = list(map(int, input(f"Introdueix una llista de numeros separada per espais ").split()))
resultat = 0
for i in llista:
    if i > resultat:
        resultat = i
print(resultat)