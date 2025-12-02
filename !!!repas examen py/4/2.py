frase = input(f"Introdueix una frase ")
contador = 0
VOCALS = ["a","e","i","o","u","A","E","I","O","U"]
for i in frase:
    if i in VOCALS:
        contador += 1
print(f"Hi han {contador} vocals")