# Què fa el programa:
# Autor: Biel Rull Simon

import math

class Cercle:
    def __init__(self, radi):
        self.radi = radi
    
    def area(self):
        return math.pi * self.radi ** 2

    def perimetre(self):
        return 2 * math.pi * self.radi

c1 = Cercle(100)

print(f"Àrea: {c1.area()}")
print(f"Perímetre: {c1.perimetre()}")
