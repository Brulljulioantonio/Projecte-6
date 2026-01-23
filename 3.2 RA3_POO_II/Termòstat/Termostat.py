# Autor: Biel Rull Simon
# Descripció: Aquest programa crea un termostat amb un atribut privat __temperatura.
# Permet:
# 1. Consultar la temperatura amb un getter
# 2. Canviar la temperatura amb un setter
# 3. Validar que la temperatura sigui sempre entre 10 i 30 °C

class Termostat:
    def __init__(self, temperatura_inicial):
        # Constructor de la classe
        # S'executa quan es crea un objecte de Termostat
        # Inicialitza l'atribut privat __temperatura amb la temperatura donada
        self.__temperatura = temperatura_inicial

    @property
    def temperatura(self):
        # Getter de la temperatura
        # Permet accedir a la temperatura amb termostat.temperatura
        # No canvia el valor, només el retorna
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        # Setter de la temperatura
        # Permet modificar la temperatura només si està entre 10 i 30 °C
        if 10 <= valor <= 30:
            self.__temperatura = valor
            print(f"Temperatura canviada a {self.__temperatura}°C")
        else:
            # Si el valor és fora del rang vàlid, mostra un missatge d'error
            print("Error: la temperatura ha de ser entre 10 i 30 °C")
