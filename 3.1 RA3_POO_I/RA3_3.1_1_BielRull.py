# Què fa el programa:
# Autor: Biel Rull Simon

class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any
    
    def mostrar_info(self):
        print(f"{self.marca} {self.model} ({self.any})")

c1 = Cotxe("Toyota", "Corolla", "2018")
c2 = Cotxe("Ford", "Fiesta", 2016)

c1.mostrar_info()
c2.mostrar_info()