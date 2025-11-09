# Què fa el programa:
# Autor: Biel Rull Simon

import Conversions

temperatures = float(input("Introdueix una temperatura en graus Celsius o Fahrenheit: "))

print(Conversions.celsius_a_fahrenheit(temperatures), "Fº")
print(Conversions.fahrenheit_a_celsius(temperatures), "Cº")