# Autor: Biel Rull Simon
# Descripció: Exemple de polimorfisme amb figures geomètriques utilitzant la biblioteca turtle.

import turtle

class Figura:
    def dibuixar(self):
        pass

class Cercle(Figura):
    def dibuixar(self):
        turtle.circle(50)

class Triangle(Figura):
    def dibuixar(self):
        for i in range(3):
            turtle.forward(200)
            turtle.left(120)

class Quadrat(Figura):
    def dibuixar(self):
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)

def fer_dibuix(figura):
    figura.dibuixar()

c = Cercle()
t = Triangle()
q = Quadrat()

fer_dibuix(c)
fer_dibuix(t)
fer_dibuix(q)