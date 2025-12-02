llista = list(map(int, input("Introdueix una llista de numeros: ").split()))
parell = []
senar = []

for i in llista:
    if i % 2 == 0:
        parell.append(i)
    else:
        senar.append(i)
print(f"Números parells: {parell}")
print(f"Números senars: {senar}")