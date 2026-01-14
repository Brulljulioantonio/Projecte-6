# Què fa el programa:
# Autor: Biel Rull Simon
# Descripció: Aquest fitxer defineix la classe Cotxe, que permet crear
# objectes representant cotxes amb marca, model i any de fabricació,
# i mostrar la seva informació.

class Cotxe:
    def __init__(self, marca, model, any):
        """
        Constructor de la classe Cotxe.
        Atributs:
        - marca: marca del cotxe (ex. "Toyota")
        - model: model del cotxe (ex. "Corolla")
        - any: any de fabricació (ex. 2020)
        
        Exemple d'ús:
        c1 = Cotxe("Toyota", "Corolla", 2020)
        """
        self.marca = marca
        self.model = model
        self.any = any
    
    def mostrar_info(self):
        """
        Mètode que mostra la informació completa del cotxe
        en un format llegible: Marca Model (Any)
        Exemple de sortida: "Toyota Corolla (2020)"
        """
        print(f"{self.marca} {self.model} ({self.any})")

# Exemple d'ús:
# c1 = Cotxe("Toyota", "Corolla", 2020)
# c1.mostrar_info()
