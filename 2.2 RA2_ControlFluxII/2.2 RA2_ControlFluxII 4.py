# Què fa el programa: 
# Autor: Biel Rull Simon
# Data: 

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