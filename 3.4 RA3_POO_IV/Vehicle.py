# Autor: Biel Rull Simon
# Descripció: Implementació de classes Vehicle i Cotxe amb herència en Python.

class Vehicle:
    def __init__(self, marca):
        self.marca = marca
    
    def arrencar(self):
        print(f"Ha arrencat el {self.marca}")

class Cotxe(Vehicle):
    def tocar_claxon(self):
        print(f"Pip pip!")

marca = "Toyota"

v = Vehicle(marca)
v.arrencar()
c = Cotxe(marca)
c.tocar_claxon()