while True:
    try:
        num = int(input(f"Introdueix un número: "))
        if num % 2 == 0:
            print(f"Es parell")
        elif num % 2 != 0:
            print(f"Es senar")
        break

    except ValueError:
        print(f"Valor no valid")