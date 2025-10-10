# Què fa el programa: comprova quin numero es mes gran
# Autor: Biel Rull Simon
# Data: 1/10/25

# Versió 1.0

num1 = int(input("introdueix el número 1: "))
num2 = int(input("introdueix el número 2: "))
num3 = int(input("introdueix el número 3: "))

if num1 > num2 and num1 > num3:
    print("el número 1 es mes gran")
elif num2 > num1 and num2 > num3:
    print("el número 2 es mes gran")
elif num3 > num1 and num3 > num2:
    print("el número 3 es mes gran")
else:
    print("son iguals")
