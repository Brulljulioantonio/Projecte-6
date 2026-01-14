# Què fa el programa:
# Autor: Biel Rull Simon
# Descripció: Aquest fitxer defineix la classe Animal i la classe Gos que hereta d'Animal.
# Permet crear animals amb nom i espècie, fer-los "fer un soroll" i especialitzar el soroll
# per als gossos.

class Animal:
    def __init__(self, nom, espècie):
        """
        Constructor de la classe Animal.
        Atributs:
        - nom: nom de l'animal (ex. "Toby")
        - espècie: tipus d'animal (ex. "gos")
        """
        self.nom = nom
        self.espècie = espècie

    def fer_soroll(self):
        """
        Mètode que mostra un soroll genèric per qualsevol animal.
        Exemple de sortida: "Toby el gos fa un soroll"
        """
        print(f"{self.nom} el {self.espècie} fa un soroll")


class Gos(Animal):
    """
    Classe Gos que hereta d'Animal.
    Sobreescriu el mètode fer_soroll per fer un soroll específic de gos.
    """
    def __init__(self, nom):
        """
        Constructor de la classe Gos.
        Només cal passar el nom; l'espècie es defineix automàticament com 'gos'.
        """
        super().__init__(nom, "gos")  # crida el constructor de la classe base

    def fer_soroll(self):
        """
        Mètode que mostra el soroll específic d'un gos.
        Exemple de sortida: "Toby fa Bup bup!"
        """
        print(f"{self.nom} fa Bup bup!")


# Exemple d'ús correcte:
#a1 = Animal("Canito", "porc")
#g1 = Gos("Dani")  # Només passem el nom, l'espècie ja és 'gos'

#a1.fer_soroll()  # Sortida: Canito el porc fa un soroll
#g1.fer_soroll()  # Sortida: Dani fa Bup bup!
