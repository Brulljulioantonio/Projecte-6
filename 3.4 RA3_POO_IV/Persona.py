# Autor: Biel Rull Simon
# Descripció: Implementa una jerarquia de classes per a persones i treballadors.

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat
        
    def saludar(self):
        print(f"Hola soc {self.nom}")
        
class Treballador(Persona):
    def __init__(self, feina):
        self.feina = feina
    
    def mostrar_feina(self):
        print(f"Treballo de {self.feina}")

nom = "Carlos"
edat = "27"
feina = "bomber"

p = Persona(nom, edat)
t = Treballador(feina)

p.saludar()
t.mostrar_feina()