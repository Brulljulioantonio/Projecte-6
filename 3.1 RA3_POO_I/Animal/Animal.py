# Què fa el programa:
# Autor: Biel Rull Simon
# Descripció: Aquest fitxer defineix la classe Animal amb atributs i mètodes per 
# representar animals i fer-los "fer un soroll". 
# Les dades (nom i espècie) poden venir d'un altre fitxer o d'entrada de l'usuari.

class Animal:
    def __init__(self, nom, espècie):
        """
        Constructor de la classe Animal.
        Inicialitza els atributs:
        - nom: nom de l'animal (per exemple, "Toby")
        - espècie: tipus d'animal (per exemple, "gos")
        
        Quan es crea un objecte de tipus Animal, s'han de passar aquests dos valors.
        """
        self.nom = nom
        self.espècie = espècie

    def fer_soroll(self):
        """
        Mètode que simula que l'animal fa un soroll.
        Actualment imprimeix un text genèric que inclou el nom i l'espècie.
        Exemple de sortida: "Toby el gos fa un soroll"
        
        Si les dades venen d'un altre fitxer, només cal crear objectes Animal
        amb els valors corresponents i cridar aquest mètode.
        """
        print(f"{self.nom} el {self.espècie} fa un soroll")

# Exemple d'ús:
# Si tinguéssim un altre fitxer amb dades d'animals, podríem fer:
# a1 = Animal(dades['nom'], dades['espècie'])
# a1.fer_soroll()
