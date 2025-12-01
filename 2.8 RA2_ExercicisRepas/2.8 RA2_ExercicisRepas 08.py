# Què fa el programa:
# Autor: Biel Rull Simon

frase = "HhOoLlAa QqUuEe TtAaLl?"
resultat = ""

for i in frase:
    if not i.islower():
        resultat += i

print(resultat)
