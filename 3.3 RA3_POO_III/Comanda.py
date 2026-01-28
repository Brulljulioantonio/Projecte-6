# Autor: Biel Rull Simon
# Descripció: Implementació d'una classe Comanda que utilitza un notificador per enviar notificacions.

class EmailNotificador:
    def enviar(self,missatge):
        print(f"Enviant email: {missatge}")
        
        
class Comanda:
    def __init__(self, client, notificador):
        self.client = client
        self.notificador = notificador
    
    def confirmar(self):
        print(f"Comanda confirmada per {self.client}")
        self.notificador.enviar(f"Hola {self.client}, la teva comanda ha estat confirmada.")
    
notificador = EmailNotificador()
comanda = Comanda("Misco", notificador)
comanda.confirmar()