# Autor: Biel Rull Simon
# Descripció: Implementa el patró de disseny Strategy per enviar missatges a través de diferents canals (Email, SMS, WhatsApp).

class Missatger:
    def __init__(self, missatgers, missatge):
        self.missatgers = missatgers
        self.missatge = missatge

    def enviar(self):
        print(f"{self.missatgers}\n{self.missatge}\n")

class Email(Missatger):
    def enviar(self):
        print(f"{self.missatgers}\n{self.missatge}\n")

class SMS(Missatger):
    def enviar(self):
        print(f"{self.missatgers}: {self.missatge}\n")

class Whatsapp(Missatger):
    def enviar(self):
        print(f"{self.missatgers}:\n{self.missatge}\n")

def enviar_missatges(tipus):
    tipus.enviar()

missatgers = "Carlos"
missatge = "Hola :)"

email = Email(missatgers, missatge)
sms = SMS(missatgers, missatge)
whatsapp = Whatsapp(missatgers, missatge)

enviar_missatges(email)
enviar_missatges(sms)
enviar_missatges(whatsapp)