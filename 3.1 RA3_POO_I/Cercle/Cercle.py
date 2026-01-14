# Què fa el programa:
# Autor: Biel Rull Simon
# Descripció: Aquest fitxer defineix la classe Cercle, que permet crear 
# objectes representant cercles amb un determinat radi i calcular-ne 
# l'àrea i el perímetre.

import math  # S'importa el mòdul math per poder utilitzar la constant pi i funcions matemàtiques

class Cercle:
    def __init__(self, radi):
        """
        Constructor de la classe Cercle.
        Atributs:
        - radi: el radi del cercle (nombre positiu)
        
        Quan es crea un objecte Cercle, cal passar el valor del radi.
        Exemple: c = Cercle(5)
        """
        self.radi = radi
    
    def area(self):
        """
        Calcula i retorna l'àrea del cercle.
        Fórmula: area = π * radi^2
        Exemple: si radi = 3, area = π * 3^2 = 28.27 aproximadament
        """
        return math.pi * self.radi ** 2

    def perimetre(self):
        """
        Calcula i retorna el perímetre (circumferència) del cercle.
        Fórmula: perimetre = 2 * π * radi
        Exemple: si radi = 3, perimetre = 2 * π * 3 = 18.85 aproximadament
        """
        return 2 * math.pi * self.radi

# Exemple d'ús:
# c1 = Cercle(5)
# print("Àrea:", c1.area())
# print("Perímetre:", c1.perimetre())
