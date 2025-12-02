try:
    num = int(input(f"Introdueix un numero "))
    for i in range(0, num+1, 2):
        print(i)
except ValueError:
    print(f"Valor no valid")