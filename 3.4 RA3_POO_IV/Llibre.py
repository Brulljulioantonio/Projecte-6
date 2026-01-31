# Autor: Biel Rull Simon
# Descripció: Implementa una jerarquia de classes per a llibres amb diferents formats.

class Llibre:
    def __init__(self, titol, autor):
        self.titol = titol
        self.autor = autor

    def mostrar_info(self):
        print(f"El nom del llibre es {self.titol} i l'autor es {self.autor}")

class LlibrePaper(Llibre):
    def __init__(self, titol, autor, n_pagines):
        super().__init__(titol, autor)
        self.n_pagines = n_pagines
    
    def mostrar_info(self):
        print(f"El nom del llibre es {self.titol} i l'autor es {self.autor} amb {self.n_pagines} de pagines")

class LlibreDigital(Llibre):
    def __init__(self, titol, autor, format):
        super().__init__(titol, autor)
        self.format = format
    
    def mostrar_info(self):
        print(f"El nom del llibre es {self.titol} que esta en format {self.format} i l'autor es {self.autor}")

titol = "sakanigadik"
autor = "Canito"
pagines = 143
format = "PDF"

l = Llibre(titol, autor)
l.mostrar_info()

lp = LlibrePaper(titol, autor, pagines)
lp.mostrar_info()

ld = LlibreDigital(titol, autor, format)
ld.mostrar_info()