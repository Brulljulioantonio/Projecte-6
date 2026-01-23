# Autor: Biel Rull Simon
# Descripció: Aquesta classe Usuari permet gestionar la contrasenya
# amb un getter i un setter. El setter comprova que la contrasenya tingui
# almenys 8 caràcters.

class Usuari:
    def __init__(self, contrasenya):
        # Constructor: inicialitza l'atribut privat __contrasenya
        self.__contrasenya = contrasenya

    @property
    def contrasenya(self):
        # Getter: permet llegir la contrasenya
        return self.__contrasenya

    @contrasenya.setter
    def contrasenya(self, clau):
        # Setter: permet canviar la contrasenya només si és vàlida
        if len(clau) >= 8:  # Comprovem que tingui almenys 8 caràcters
            self.__contrasenya = clau
            print("Contrasenya canviada correctament")
        else:
            print("Error: contrasenya no valida")
