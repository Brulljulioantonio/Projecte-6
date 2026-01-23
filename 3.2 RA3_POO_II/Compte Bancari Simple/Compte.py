# Autor: Biel Rull Simon
# Descripció: Aquest programa crea un compte bancari amb un saldo inicial i permet:
# 1. Ingressar diners al compte
# 2. Retirar diners del compte
# 3. Consultar el saldo actual del compte
# Els moviments actualitzen el saldo i el mostren per pantalla.

class Compte:
    def __init__(self, saldo):
        # Constructor de la classe:
        # S'executa quan es crea un objecte de Compte.
        # Inicialitza el saldo del compte amb el valor donat.
        # __saldo és un atribut privat, només accessible dins de la classe.
        self.__saldo = saldo

    def ingressar(self, quantitat):
        # Ingressa diners al compte
        # S'afegeix la quantitat al saldo actual
        self.__saldo = self.__saldo + quantitat
        # Mostra el nou saldo després de l'ingrés
        print(f"{self.__saldo}€")

    def retirar(self, quantitat):
        # Retira diners del compte
        # Es resta la quantitat del saldo actual
        self.__saldo = self.__saldo - quantitat
        # Mostra el nou saldo després de la retirada
        print(f"{self.__saldo}€")

    def consultar(self):
        # Mostra el saldo actual del compte
        print(f"{self.__saldo}€")
