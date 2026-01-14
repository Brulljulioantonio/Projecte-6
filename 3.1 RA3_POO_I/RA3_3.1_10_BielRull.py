# Què fa el programa:
# Autor: Biel Rull Simon

import math

class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, altre_punt):
        dx = altre_punt.x - self.x
        dy = altre_punt.y - self.y
        return math.sqrt(dx**2 + dy**2)
    
p1 = Punt(12, -7)

p1.distancia()