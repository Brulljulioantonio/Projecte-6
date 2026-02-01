# Autor: Biel Rull Simon
# Descripció: 

class Animal:
    def fer_soroll(self):
        print(f"L'animal fa un soroll")

class Gat(Animal):
    def fer_soroll(self):
        print(f"Miau")

class Vaca(Animal):
    def fer_soroll(self):
        print(f"Muu")

def reproduir_soroll(animal):
    animal.fer_soroll()

g = Gat()
v = Vaca()

reproduir_soroll(g)
reproduir_soroll(v)