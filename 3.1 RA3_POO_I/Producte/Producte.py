# Què fa el programa:
# Autor: Biel Rull Simon
# Descripció: Aquest fitxer defineix la classe Producte, que permet crear objectes
# amb nom i preu, i oferir informació sobre el preu normal i un preu amb rebaixa del 50%.

class Producte:
    def __init__(self, nom, preu):
        """
        Constructor de la classe Producte.
        Atributs:
        - nom: nom del producte (ex. "Llapis")
        - preu: preu del producte (ex. 2.50)
        
        Exemple:
        p1 = Producte("Llapis", 2.5)
        """
        self.nom = nom
        self.preu = preu
    
    def productes(self):
        """
        Mètode que mostra el preu normal del producte.
        Exemple de sortida:
        "Llapis 2.5 Preu normal"
        """
        print(f"{self.nom} {self.preu} Preu normal")
    
    def percentatge(self):
        """
        Mètode que mostra el preu del producte amb un descompte del 50%.
        Calcula el 50% del preu i ho imprimeix.
        Exemple de sortida:
        "Llapis 1.25 Rebaixa 50%"
        """
        print(f"{self.nom} {self.preu * 0.5} Rebaixa 50%")

# Exemple d'ús:
# p1 = Producte("Llapis", 2.5)
# p1.productes()    # Mostra el preu normal
# p1.percentatge()  # Mostra el preu amb rebaixa
