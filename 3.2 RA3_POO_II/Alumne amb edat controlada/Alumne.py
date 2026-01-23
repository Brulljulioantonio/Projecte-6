# Autor: Biel Rull Simon
# Descripció: Aquesta classe Alumne gestiona l'edat d'un alumne.
# Permet:
# 1. Llegir l'edat amb un getter
# 2. Modificar l'edat amb un setter que no accepta valors negatius

class Alumne:
    def __init__(self, edat):
        # Constructor: inicialitza l'atribut privat __edat
        self.__edat = edat

    @property
    def edat(self):
        # Getter: retorna l'edat de l'alumne
        return self.__edat

    @edat.setter
    def edat(self, nova_edat):
        # Setter: només permet edats no negatives
        if nova_edat >= 0:
            self.__edat = nova_edat
        else:
            print("Error: l'edat no pot ser negativa")
