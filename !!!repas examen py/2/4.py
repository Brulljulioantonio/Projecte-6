import random
intent = 0
num = random.randint(0,10)
while num != intent:
    intent = int(input(f"Introdueix un número: "))
    if intent == num:
            print(f"Correcte")
    else:
            print(f"Incorrecte")