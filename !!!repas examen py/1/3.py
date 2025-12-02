while True:
    try:
        n1 = int(input(f"Introdueix valor 1: "))
        n2 = int(input(f"Introdueix valor 2: "))
        n3 = int(input(f"Introdueix valor 3: "))
        
        if n1 > n2 and n1 > n3:
            print(f"{n1} es mes gran")
        elif n2 > n1 and n2 > n3:
            print(f"{n2} es mes gran")
        elif n3 > n1 and n3 > n2:
            print(f"{n3} es mes gran")
        elif n1 == n2 and n1 == n3:
            print(f"Son iguals")
        break
    except ValueError:
        print(f"Valor no valid")