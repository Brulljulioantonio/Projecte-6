while True:
    try:
        nota = int(input(f"Introdueix una nota del 1-10: "))
        if nota in range(1,11):
            if nota >= 5:
                print(f"aprobat")
            elif nota < 5:
                print(f"suspes")
            break
        else:
            print(f"Valor no valid")
    except ValueError:
        print(f"Valor no valid")