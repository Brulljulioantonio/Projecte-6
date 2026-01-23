class Sensor:
    def __init__(self, valor):
        self.__valor = valor
        
    @property
    def v_sensor(self):
        return self.__valor
    
    @v_sensor.setter
    def v_sensor(self, n_valor):
        if 0 <= n_valor <= 100:

            self.__valor = n_valor
        else:
            print("El valor ha de estar entre 0 i 100")