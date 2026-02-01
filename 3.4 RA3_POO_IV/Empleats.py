# Autor: Biel Rull Simon
# Descripció: 

class Empleat:
    def calcular_sou(self):
        pass

class Fixe(Empleat):
    def __init__(self, salari_base):
        self.salari_base = salari_base
    
    def calcular_sou(self):
        print(self.salari_base)

class Autonom(Empleat):
    def __init__(self, hores, preu_hora):
        self.hores = hores
        self.preu_hora = preu_hora

    def calcular_sou(self):
        print(f"{(self.hores * self.preu_hora) * 30}€")

def mostrar_sous(tipus):
    tipus.calcular_sou()

sb = "1200€"
f = Fixe(sb)

h = 8
ph = 7
a = Autonom(h, ph)

mostrar_sous(f)
mostrar_sous(a)