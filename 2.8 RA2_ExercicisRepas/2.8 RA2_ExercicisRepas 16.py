# Què fa el programa:
# Autor: Biel Rull Simon

while True:
    try:
        num = int(input("Introdueix un número: "))
        print(num)
        break
    
    except ValueError:
        print("Valor no valid, introdueix un número valid")