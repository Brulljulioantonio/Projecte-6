class Usuari:
    def __init__(self, contrasenya):
        self.__contrasenya = contrasenya

    @property
    def contrasenya(self):
        return self.__contrasenya

    @contrasenya.setter
    def contrasenya(self, clau):
        if self.len_minim(clau) and self.w_upper(clau) and self.w_num(clau):
            self.__contrasenya = clau
            print("Contrasenya canviada correctament")
        else:
            print("Error: contrasenya no vàlida")

    # Validacions
    def len_minim(self, clau):
        return len(clau) >= 8

    def w_upper(self, clau):
        return any(i.isupper() for i in clau)

    def w_num(self, clau):
        return any(i.isdigit() for i in clau)
