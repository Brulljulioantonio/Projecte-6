try:
    num = int(input("Introdueix un número "))

    if num < 0:
        print(f"{num} es mes petit que 0")
    elif num > 0:
        print(f"{num} es mes gran que 0")
    elif num == 0:
        print(f"{num} es igual a 0")
        
except ValueError:
    print("Valor no valid")