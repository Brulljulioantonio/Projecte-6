# Què fa el programa: Escriu una funció area_rectangle(base, altura) que retorni l'àrea (base * altura).
# Autor: Biel Rull Simon

base = float(input("Introdueix la base del rectangle: "))
altura = float(input("Introdueix l'altura del rectangle: "))

def area_rectangle(base, altura):
    area = base * altura
    return area
print("L'àrea del rectangle és:", area_rectangle(base, altura))