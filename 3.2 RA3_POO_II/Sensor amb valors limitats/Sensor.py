# Autor: Biel Rull Simon
# Descripció: Aquesta classe Sensor gestiona un valor del sensor entre 0 i 100.
# Permet:
# 1. Llegir el valor amb un getter
# 2. Modificar el valor amb un setter amb control de rang

class Sensor:
    def __init__(self, valor):
        # Constructor de la classe
        # Inicialitza l'atribut privat __valor amb el valor inicial
        self.__valor = valor
        
    @property
    def v_sensor(self):
        # Getter: permet llegir el valor del sensor
        # No modifica el valor, només el retorna
        return self.__valor
    
    @v_sensor.setter
    def v_sensor(self, n_valor):
        # Setter: permet canviar el valor del sensor només si està entre 0 i 100
        if 0 <= n_valor <= 100:
            self.__valor = n_valor
        else:
            # Si el valor no és vàlid, mostra un missatge d'error
            print("Error: el valor ha d'estar entre 0 i 100")
