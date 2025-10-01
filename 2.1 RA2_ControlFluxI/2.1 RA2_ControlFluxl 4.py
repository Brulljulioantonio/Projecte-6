# Què fa el programa: comprova si estas aprobat o no
# Autor: Biel Rull Simon
# Data: 1/10/25

# Versió 1.0

nota = int(input("introdueix nota del 1 al 10: "))

if nota >= 5:
    print("aprobat")
if nota < 5:
    print("suspès")