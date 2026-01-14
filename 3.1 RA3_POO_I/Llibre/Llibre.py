# Què fa el programa:
# Autor: Biel Rull Simon
# Descripció: Aquest fitxer defineix la classe Llibre, que permet crear objectes
# representant llibres amb títol, autor i any de publicació, i mostrar aquesta informació.

class Llibre:
    def __init__(self, titol, autor, any):
        """
        Constructor de la classe Llibre.
        Atributs:
        - titol: títol del llibre (ex. "El Quixot")
        - autor: nom de l'autor (ex. "Miguel de Cervantes")
        - any: any de publicació (ex. 1605)
        
        Exemple d'ús:
        l1 = Llibre("El Quixot", "Miguel de Cervantes", 1605)
        """
        self.titol = titol
        self.autor = autor
        self.any = any

    def mostrar_info(self):
        """
        Mètode que mostra tota la informació del llibre de manera llegible.
        Cada atribut s'imprimeix en una línia diferent utilitzant salts de línia (\n).
        
        Exemple de sortida:
        Titol: El Quixot
        Autor: Miguel de Cervantes
        Any: 1605
        """
        print(f" Titol: {self.titol}\n Autor: {self.autor}\n Any: {self.any}")

# Exemple d'ús:
# l1 = Llibre("El Quixot", "Miguel de Cervantes", 1605)
# l1.mostrar_info()
