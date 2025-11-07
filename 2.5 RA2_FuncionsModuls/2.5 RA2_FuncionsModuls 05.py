# Què fa el programa: Escriu una funció saluda_nom(nom="amic") que imprimeixi "Hola, <nom>". Si no passes cap nom, ha de imprimir "Hola, amic".
# Autor: Biel Rull Simon

nom = input("Introdueix el teu nom: ")

def saluda_nom(nom="amic"):
    if nom == "":
        nom = "amic"
    print("Hola", nom)
    return
saluda_nom(nom)