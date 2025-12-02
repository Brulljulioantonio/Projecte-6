frase = input(f"Introdueix una frase ")
alreves = ""

for i in frase:
    alreves = frase[::-1]
if frase == alreves:
    print(f"es un palindrom")
else:
    print(f"no es un palindrom")