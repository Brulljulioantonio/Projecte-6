# Autor: Biel Rull Simon
# Descripció: Aquesta classe Joc gestiona la puntuació d'un jugador.
# Permet:
# 1. Llegir la puntuació amb un getter
# 2. Afegir punts a la puntuació
# 3. Reiniciar la puntuació

class Joc:
    def __init__(self):
        # Constructor: inicialitza la puntuació a 0
        self.__puntuacio = 0

    @property
    def puntuacio(self):
        # Getter: retorna la puntuació actual
        return self.__puntuacio

    def sumar_punts(self, punts):
        # Afegeix punts a la puntuació actual
        if punts > 0:
            self.__puntuacio += punts
        else:
            print("Error: els punts a afegir han de ser positius")

    def reiniciar(self):
        # Reinicia la puntuació a 0
        self.__puntuacio = 0
