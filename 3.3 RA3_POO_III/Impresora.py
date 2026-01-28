# Autor: Biel Rull Simon
# Descripció: Implementació d'una classe Factura que utilitza una impressora per imprimir el contingut de la factura.

class ImpressoraPDF:
    def imprimir(self, contingut):
        print(f"Imprimint PDF: {contingut}")
        
class Factura:
    def __init__(self, client, import_total, impressora):
        self.client = client
        self.import_total = import_total
        self.impressora = impressora
        
    def imprimir_factura(self):
        contingut = f"Factura per a {self.client}, total: {self.import_total} €"
        self.impressora.imprimir(contingut)

impressora = ImpressoraPDF()
factura = Factura("Biel Rull", 100, impressora)
factura.imprimir_factura()