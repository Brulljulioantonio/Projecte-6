# Què fa el programa:
# Autor: Biel Rull Simon

class CompteBancari:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def ingresar(self):
        print(f"Quantitat a ingresar")
        quantitat = int(input())
        self.saldo = self.saldo + quantitat
        print(f"Tens {self.saldo}€")
        
    def retirar(self):
        print(f"Quantitat a retirar")
        quantitat = int(input())
        self.saldo = self.saldo - quantitat
        print(f"Tens {self.saldo}€")
        
    def veure_saldo(self):
        print(f"Tens {self.saldo}€")

cb1 = CompteBancari(100)

cb1.retirar()