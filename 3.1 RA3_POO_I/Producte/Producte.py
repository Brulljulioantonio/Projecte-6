# Què fa el programa:
# Autor: Biel Rull Simon

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu
    
    def productes(self):
        print(f"{self.nom} {self.preu} Preu normal")
    
    def percentatge(self):
        print(f"{self.nom} {self.preu * 0.5} Rebaixa 50%")