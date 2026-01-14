# Què fa el programa:
# Autor: Biel Rull Simon

class Animal:
    def __init__(self, nom, espècie):
        self.nom = nom
        self.espècie = espècie

    def fer_soroll(self):
        print(f"{self.nom} el {self.espècie} fa un soroll")

a1 = Animal("Canito", "porc")

a1.fer_soroll()