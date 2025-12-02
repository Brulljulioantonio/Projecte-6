frase = input(f"Introdueix una frase ")
resultat = ""

for i in frase:
    if i == " ":
        resultat += ""
    else:
        resultat += i
print(resultat)