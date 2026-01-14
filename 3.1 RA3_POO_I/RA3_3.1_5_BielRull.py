# Què fa el programa:
# Autor: Biel Rull Simon

class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota
    
    def Nota_es(self):
        if self.nota >= 5:
            print(f"{self.nom} aprobat")
        else:
            print(f"{self.nom} suspès")
        
e1 = Estudiant("Carlos", 4)

e1.Nota_es()
