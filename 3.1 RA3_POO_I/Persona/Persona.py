# Què fa el programa:
# Autor: Biel Rull Simon
# Descripció: Aquest fitxer defineix la classe Persona, que permet crear objectes
# amb nom i edat, i un mètode per presentar-se imprimint aquesta informació.

class Persona:
    def __init__(self, nom, edat):
        """
        Constructor de la classe Persona.
        Atributs:
        - nom: nom de la persona (ex. "Anna")
        - edat: edat de la persona (ex. 25)
        
        Exemple d'ús:
        p1 = Persona("Anna", 25)
        """
        self.nom = nom
        self.edat = edat
    
    def presentar_se(self):
        """
        Mètode que mostra una presentació de la persona.
        Exemple de sortida:
        "Hola soc Anna i tinc 25 anys"
        """
        print(f"Hola soc {self.nom} i tinc {self.edat} anys")

# Exemple d'ús:
# p1 = Persona("Anna", 25)
# p1.presentar_se()
