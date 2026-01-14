# Què fa el programa:
# Autor: Biel Rull Simon
# Descripció: Aquest fitxer defineix la classe Estudiant, que permet crear
# objectes amb nom i nota d'un estudiant, i determinar si ha aprovat o suspès.

class Estudiant:
    def __init__(self, nom, nota):
        """
        Constructor de la classe Estudiant.
        Atributs:
        - nom: nom de l'estudiant (per exemple, "Maria")
        - nota: nota de l'estudiant (nombre enter o decimal)
        
        Exemple:
        e1 = Estudiant("Maria", 7)
        """
        self.nom = nom
        self.nota = nota
    
    def Nota_es(self):
        """
        Mètode que comprova si l'estudiant ha aprovat o suspès.
        Condició:
        - Si la nota >= 5 → aprovat
        - Si la nota < 5 → suspès
        Mostra el resultat amb un missatge que inclou el nom de l'estudiant.
        
        Exemple de sortida:
        "Maria aprovat" o "Joan suspès"
        """
        if self.nota >= 5:
            print(f"{self.nom} aprovat")
        else:
            print(f"{self.nom} suspès")

# Exemple d'ús:
# e1 = Estudiant("Maria", 7)
# e1.Nota_es()   # Sortida: Maria aprovat
# e2 = Estudiant("Joan", 4)
# e2.Nota_es()   # Sortida: Joan suspès
