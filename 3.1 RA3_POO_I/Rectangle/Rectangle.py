# Què fa el programa:
# Autor: Biel Rull Simon
# Descripció: Aquest fitxer defineix la classe Rectangle, que permet crear
# objectes representant rectangles amb amplada i alçada, i calcular-ne
# l'àrea i el perímetre.

class Rectangle:
    def __init__(self, amplada, alçada):
        """
        Constructor de la classe Rectangle.
        Atributs:
        - amplada: amplada del rectangle (nombre)
        - alçada: alçada del rectangle (nombre)
        
        Exemple:
        r1 = Rectangle(5, 10)
        """
        self.amplada = amplada
        self.alçada = alçada
    
    def area(self):
        """
        Mètode que calcula i mostra l'àrea del rectangle.
        Fórmula: area = amplada * alçada
        Exemple:
        Si amplada = 5 i alçada = 10, area = 50
        """
        print(self.amplada * self.alçada)
    
    def perimetre(self):
        """
        Mètode que calcula i mostra el perímetre del rectangle.
        Fórmula: perimetre = 2 * (amplada + alçada)
        Exemple:
        Si amplada = 5 i alçada = 10, perímetre = 30
        """
        print(2 * (self.amplada + self.alçada))

# Exemple d'ús:
# r1 = Rectangle(5, 10)
# r1.area()       # Sortida: 50
# r1.perimetre()  # Sortida: 30
