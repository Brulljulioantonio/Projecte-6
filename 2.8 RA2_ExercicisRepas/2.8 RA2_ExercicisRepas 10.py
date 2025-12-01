# Què fa el programa:
# Autor: Biel Rull Simon

valors = list(map(int, input("Introdueix valors separats per espais o comes: ").split()))
num_busca = int(input("Introdueix el número a buscar: "))
contador = 0

for i in valors:
    if i == num_busca:
        contador += 1
print("El número", num_busca ,"esta repetit", contador ,"vegades")