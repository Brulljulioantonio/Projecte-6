# Què fa el programa:
# Autor: Biel Rull Simon

class Llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any

    def mostrar_info(self):
        print(f" Titol: {self.titol}\n Autor: {self.autor}\n Any: {self.any}")

l1 = Llibre("Canito maricon", "Canito", 1945)

l1.mostrar_info()