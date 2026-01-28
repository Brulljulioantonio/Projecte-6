# Autor: Biel Rull Simon
# Descripció: Exercici d'herència i polimorfisme amb classes d'animals

class Animal:
    def parlar(self):
        print("L'animal fa un so")

class Gos(Animal):
    def parlar(self):
        print("El gos fa un so")
        
class Gat(Animal):
    def parlar(self):
        print("El Gat fa un so")

a = Animal()
go = Gos()
ga = Gat()

a.parlar()
go.parlar()
ga.parlar()