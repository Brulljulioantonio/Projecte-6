# Autor: Biel Rull Simon
# Descripció: Exercici d'herència i polimorfisme amb classes d'animals

class Animal:
    def parlar(self):
        print("L'animal fa un so")

class Gos(Animal):
    def parlar(self):
        print("bup bup")
        
class Gat(Animal):
    def parlar(self):
        print("miau miau")

a = Animal()
go = Gos()
ga = Gat()

a.parlar()
go.parlar()
ga.parlar()