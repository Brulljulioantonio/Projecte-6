llista = input("introdueix una llista de paraules: ").split()
VOCALS = ["a","e","i","o","u","A","E","I","O","U"]
resultat = []
for i in llista:
    if i[0] in VOCALS:
        resultat.append(i)
print(resultat)