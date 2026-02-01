# Autor: Biel Rull Simon
# Descripció: 

class Vehicle:
    def moure(self):
        print(f"El vehicle es mou")

class Cotxe:
    def moure(self):
        print(f"El cotxe viatja per l'autovia")

class Bicicleta:
    def moure(self):
        print(f"La bicicleta es mou per la ciutat")

class Barca:
    def moure(self):
        print(f"La barca nevega per el mar")

def reproduir_soroll(i):
    i.moure()

co = Cotxe()
bi = Bicicleta()
ba = Barca()

reproduir_soroll(co)
reproduir_soroll(bi)
reproduir_soroll(ba)