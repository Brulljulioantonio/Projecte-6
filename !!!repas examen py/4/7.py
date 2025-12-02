frase = input(f"Introdueix una frase ")
contador = 0

for i in frase:
    if i == "a" or "A":
        contador += 1
print(f"Hi han {contador} lletres A")