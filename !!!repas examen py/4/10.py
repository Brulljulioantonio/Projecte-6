frase1 = "hola-"
frase2 = " -que tal?"
frases_juntes = frase1 + frase2
resultat = ""

for i in frases_juntes:
    if i == "-":
        resultat += ""
    else:
        resultat += i
print(resultat)