# Autor: Biel Rull Simon
# Descripció: 

import math

class Figura:
    def area():
        print(f"Àrea no definida")

class Quadrat(Figura):
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2
    
    def area(self):
        print(f"L'area del quadrat és: {self.c1 * self.c2}")

class Cercle(Figura):
    def __init__(self, r):
        self.r = r
    
    def area(self):
        print(f"L'area de la circumferencia es de {math.pi * (self.r ** 2)}")

q = Quadrat(2, 2)
q.area()

c = Cercle(5)
c.area()