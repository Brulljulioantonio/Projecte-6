# Què fa el programa:
# Autor: Biel Rull Simon
# Descripció: Aquest fitxer defineix la classe CompteBancari, que permet
# crear un compte amb un saldo inicial, ingressar diners, retirar-los
# i consultar el saldo actual. Les dades poden venir d'un altre fitxer
# o d'entrada de l'usuari.

class CompteBancari:
    def __init__(self, saldo):
        """
        Constructor de la classe CompteBancari.
        Atributs:
        - saldo: el saldo inicial del compte (nombre enter o decimal)
        
        Exemple: c = CompteBancari(100)
        """
        self.saldo = saldo
    
    def ingresar(self):
        """
        Mètode per ingressar diners al compte.
        1. Mostra un missatge demanant la quantitat.
        2. Llegeix la quantitat des de l'entrada de l'usuari (input).
        3. Converteix la quantitat a enter (int) i l'afegeix al saldo.
        4. Mostra el saldo actualitzat.
        """
        print(f"Quantitat a ingresar")
        quantitat = int(input())
        self.saldo = self.saldo + quantitat
        print(f"Tens {self.saldo}€")
        
    def retirar(self):
        """
        Mètode per retirar diners del compte.
        1. Mostra un missatge demanant la quantitat.
        2. Llegeix la quantitat des de l'entrada de l'usuari.
        3. Converteix la quantitat a enter (int) i la resta del saldo.
        4. Mostra el saldo actualitzat.
        
        Nota: actualment no comprova si hi ha saldo suficient.
        """
        print(f"Quantitat a retirar")
        quantitat = int(input())
        if quantitat > self.saldo:
            print(f"No tens suficient saldo")
        else:
            self.saldo = self.saldo - quantitat
            print(f"Tens {self.saldo}€")
        
    def veure_saldo(self):
        """
        Mètode per veure el saldo actual del compte.
        Simplement imprimeix el saldo guardat a l'atribut self.saldo.
        """
        print(f"Tens {self.saldo}€")
        
# Exemple d'ús:
# cb1 = CompteBancari(100)
# cb1.ingresar()    # ingressa diners al compte
# cb1.retirar()     # retira diners del compte
# cb1.veure_saldo() # mostra el saldo actual
