# Autor: Biel Rull Simon
# Descripció: Aquesta classe Rellotge gestiona les hores d'un rellotge (0-23).
# Permet:
# 1. Llegir les hores amb un getter
# 2. Modificar les hores amb un setter que només accepta 0-23
# 3. Mostrar les hores en format "HH:00"

class Rellotge:
    def __init__(self, hores):
        # Constructor: inicialitza l'atribut privat __hores
        self.__hores = hores

    @property
    def hores(self):
        # Getter: retorna les hores del rellotge
        return self.__hores

    @hores.setter
    def hores(self, n_hores):
        # Setter: només permet valors entre 0 i 23
        if 0 <= n_hores <= 23:
            self.__hores = n_hores
        else:
            print("Error: les hores han d'estar entre 0 i 23")

    def mostrar_hora(self):
        # Mètode per mostrar les hores en format "HH:00"
        # La funció zfill(2) assegura que sempre hi hagi dos dígits
        print(f"{str(self.__hores).zfill(2)}:00")
