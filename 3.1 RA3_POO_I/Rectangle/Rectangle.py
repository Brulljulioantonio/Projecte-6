# Què fa el programa:
# Autor: Biel Rull Simon

class Rectangle:
    def __init__(self, amplada, alçada):
        self.amplada = amplada
        self.alçada = alçada
    
    def area(self):
        print(self.amplada * self.alçada)
    
    def perimetre(self):
        print(2 * (self.amplada + self.alçada))