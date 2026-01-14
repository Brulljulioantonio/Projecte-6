# Què fa el programa:
# Autor: Biel Rull Simon
# Descripció: Aquest fitxer defineix la classe Punt, que representa un punt
# en un pla 2D amb coordenades (x, y), i permet calcular la distància entre
# dos punts utilitzant la fórmula de la distància euclidiana.

import math  # S'importa el mòdul math per poder utilitzar la funció sqrt

class Punt:
    def __init__(self, x, y):
        """
        Constructor de la classe Punt.
        Atributs:
        - x: coordenada x del punt (nombre)
        - y: coordenada y del punt (nombre)
        
        Exemple:
        p1 = Punt(3, 4)
        """
        self.x = x
        self.y = y

    def distancia(self, altre_punt):
        """
        Mètode que calcula la distància entre aquest punt i un altre punt.
        Fórmula de la distància euclidiana:
        distància = √((x2 - x1)^2 + (y2 - y1)^2)
        
        Paràmetre:
        - altre_punt: objecte de tipus Punt
        
        Retorna:
        - distància entre els dos punts (float)
        
        Exemple:
        p1 = Punt(0, 0)
        p2 = Punt(3, 4)
        print(p1.distancia(p2))  # Sortida: 5.0
        """
        dx = altre_punt.x - self.x
        dy = altre_punt.y - self.y
        return math.sqrt(dx**2 + dy**2)

# Exemple d'ús:
# p1 = Punt(0, 0)
# p2 = Punt(3, 4)
# print("Distància:", p1.distancia(p2))  # Sortida: 5.0
