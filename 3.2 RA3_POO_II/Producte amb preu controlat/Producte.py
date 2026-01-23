# Autor: Biel Rull Simon
# Descripció: Aquesta classe Producte gestiona un producte amb un nom públic
# i un preu privat. Permet:
# 1. Llegir el preu amb un getter
# 2. Modificar el preu amb un setter només si és positiu

class Producte:
    def __init__(self, nom, preu):
        # Constructor: inicialitza el nom públic i el preu privat
        self.nom = nom               # Nom del producte (públic)
        self.__preu = preu           # Preu del producte (privat)

    @property
    def preu(self):
        # Getter: permet llegir el preu
        return self.__preu

    @preu.setter
    def preu(self, nou_preu):
        # Setter: permet canviar el preu només si és major que 0
        if nou_preu > 0:
            self.__preu = nou_preu
            print(f"Preu del producte '{self.nom}' canviat a {self.__preu}€")
        else:
            print("Error: el preu ha de ser major que 0")
