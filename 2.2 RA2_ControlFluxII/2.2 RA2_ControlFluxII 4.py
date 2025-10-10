# Què fa el programa: genera un numero aleatori entre 1 i 100 i l'usuari ha d'endevinar-lo
# Autor: Biel Rull Simon
# Data:  8/10/25

# Versió 1.0

import random
n = random.randint(1, 100)
guess = int(input("Numero del 1-100? "))

while(n != guess):
    if guess < n:
        print("puja")

    elif guess > n:
        print("baixa")

    elif guess == n:
        print("correcte")
    
    guess = int(input("Numero del 1-100? "))

if guess == n:
    print("correcte")