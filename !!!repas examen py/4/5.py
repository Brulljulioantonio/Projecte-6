frase = input(f"Introdueix una frase ")
A = ["a","A"]
resultat = ""
for i in frase:
    if i in A:
        resultat += "@"
    else:
        resultat += i
print(resultat)