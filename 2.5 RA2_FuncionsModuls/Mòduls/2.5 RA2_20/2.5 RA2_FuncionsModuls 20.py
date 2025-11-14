# Què fa el programa:
# Autor: Biel Rull Simon

import calculadora

while True:
    print("\n--- MENÚ ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sortir")

    opcio = input("Tria una opció: ")

    if opcio == "0":
        print("Adeu!")
        break

    a = int(input("Primer número: "))
    b = int(input("Segon número: "))

    if opcio == "1":
        print("Resultat:", calculadora.suma(a, b))
    elif opcio == "2":
        print("Resultat:", calculadora.resta(a, b))
    elif opcio == "3":
        print("Resultat:", calculadora.multiplicar(a, b))
    elif opcio == "4":
        print("Resultat:", calculadora.dividir(a, b))
    else:
        print("Opció no vàlida")
