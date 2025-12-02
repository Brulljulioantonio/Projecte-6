try:
    num = int(input(f"Introdueix un número: "))
    for i in range(0,num+1):
        print(i)
except ValueError:
    print(f"Valor no valid")