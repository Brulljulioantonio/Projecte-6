# Autor: Biel Rull Simon
# Descripció: Aquest programa crea un objecte Estudiant amb una nota i permet:
# 1. Mostrar la nota si està entre 0 i 10
# 2. Mostrar un missatge d'error si la nota no és vàlida

class Estudiant:
    def __init__(self, nota):
        # Constructor de la classe:
        # S'executa quan es crea un objecte de la classe Estudiant
        # Inicialitza l'atribut _nota amb el valor donat
        self._nota = nota  # Nota de l'estudiant (atribut protegit)

    def nota(self):
        # Mètode per mostrar la nota de l'estudiant
        # Comprovem si la nota és vàlida (entre 0 i 10)
        try:
            if self._nota in range(0, 11):  # Rangs 0, 1, 2, ..., 10
                print(f"La nota és: {self._nota}")
            else:
                # Si la nota no és vàlida, generem un error manualment
                raise ValueError
        except ValueError:
            # Captura l'error i mostra un missatge amigable
            print("Error: La nota ha de ser entre 0 i 10")
