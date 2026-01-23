# Autor: Biel Rull Simon
# Descripció: Aquesta classe CompteUsuari gestiona l'email d'un usuari.
# Permet:
# 1. Llegir l'email amb un getter
# 2. Modificar l'email amb un setter que comprova que contingui '@' i '.'

class CompteUsuari:
    def __init__(self, email):
        # Constructor: inicialitza l'atribut privat __email
        self.__email = email

    @property
    def email(self):
        # Getter: retorna l'email actual
        return self.__email

    @email.setter
    def email(self, nou_email):
        # Setter: només accepta emails que continguin '@' i '.'
        if "@" in nou_email and "." in nou_email:
            self.__email = nou_email
            print(f"Email canviat a: {self.__email}")
        else:
            print("Error: email no vàlid")
