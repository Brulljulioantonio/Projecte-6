# Autor: Biel Rull Simon
# Descripció: Aquesta classe Usuari permet gestionar la contrasenya d'un usuari.
# La contrasenya es guarda en un atribut privat (__contrasenya) i es pot
# llegir amb un getter i canviar amb un setter. El setter comprova que la
# contrasenya sigui vàlida abans de modificar-la.

class Usuari:
    def __init__(self, contrasenya):
        # Constructor: inicialitza l'atribut privat __contrasenya amb la contrasenya donada
        self.__contrasenya = contrasenya

    @property
    def contrasenya(self):
        # Getter: permet llegir la contrasenya de l'usuari
        return self.__contrasenya

    @contrasenya.setter
    def contrasenya(self, clau):
        # Setter: permet canviar la contrasenya només si passa totes les validacions
        # Comprova longitud mínima, almenys una majúscula i almenys un número
        if self.len_minim(clau) and self.w_upper(clau) and self.w_num(clau):
            self.__contrasenya = clau
            print("Contrasenya canviada correctament")
        else:
            print("Error: contrasenya no vàlida")

    def len_minim(self, clau):
        return len(clau) >= 8

    def w_upper(self, clau):
        return any(i.isupper() for i in clau)

    def w_num(self, clau):
        return any(i.isdigit() for i in clau)
