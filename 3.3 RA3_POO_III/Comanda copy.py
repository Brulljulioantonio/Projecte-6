# Autor: Biel Rull Simon
# Descripció:

class Descompte20:
    def aplicar(self, preu):
        return preu * 0.2
        

class CarretCompra:
    def __init__(self, total):
        self.total = total
        
    def calcular_total_amb_descompte(self, descompte):
        return self.total - descompte
    
descompte20 = Descompte20()
carret = CarretCompra(100)
descompte = descompte20.aplicar(carret.total)

print(f"{carret.calcular_total_amb_descompte(descompte)}")
