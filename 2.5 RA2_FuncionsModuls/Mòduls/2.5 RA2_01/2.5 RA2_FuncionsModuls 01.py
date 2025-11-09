# Què fa el programa: Utilitza un mòdul anomenat Calculadora que conté funcions per a operacions bàsiques:
# Autor: Biel Rull Simon

import Calculadora

a = int(input("Introdueix el primer nombre: "))
b = int(input("Introdueix el segon nombre: "))

print("Suma:", Calculadora.suma(a, b))
print("Resta:", Calculadora.resta(a, b))
print("Multiplicació:", Calculadora.multiplicacio(a, b))
print("Divisió:", Calculadora.divisio(a, b))