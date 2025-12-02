VOCALS = ["a","e","i","o","u","A","E","I","O","U"]
contadorv = 0
contadorc = 0
lletres = 0
frase = input(f"Introdueix una frase ")
for i in frase:
        if i in VOCALS:
                contadorv += 1
        else:
                contadorc += 1
lletres = contadorc + contadorv

print(f"Hi han {contadorv} vocals")
print(f"Hi han {contadorc} consonants")
print(f"Hi han {lletres} lletres")