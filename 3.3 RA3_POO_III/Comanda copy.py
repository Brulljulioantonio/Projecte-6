# Autor: Biel Rull Simon
# Descripció:

class CarretCompra:
    def __init__(self, total):
        self.total = total

    def calcular_total_amb_descompte(self):
        descompte = self.total * 0.2
        return self.total - descompte

class Descompte20:
    def aplicar_d(self, preu):
        preu * 0.2

carretcompra = CarretCompra()
CarretCompra.calcular_total_amb_descompte(120)