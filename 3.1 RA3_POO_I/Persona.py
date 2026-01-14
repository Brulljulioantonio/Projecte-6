# Què fa el programa:
# Autor: Biel Rull Simon

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat
    
    def presentar_se(self):
        print(f"Hola soc {self.nom} i tinc {self.edat} anys")

p1 = Persona("Ramon", 19)

p1.presentar_se()