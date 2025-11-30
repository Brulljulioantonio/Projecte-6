# Què fa el programa:
# Autor: Biel Rull Simon

try:
    nota = float(input("Introdueix la teva nota: "))
    
    if nota < 0 or nota > 10:
        print("La nota ha de ser del 0-10")

    else:
        if nota < 5:
            print("NA")

        elif nota < 6.99:
            print("AS")

        elif nota < 8.99:
            print("AN")

        else:
            print("AE")
except ValueError:
    print("Valor no valid")