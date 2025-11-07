# Què fa el programa: Escriu una funció saluda_nom(nom="amic") que imprimeixi "Hola, <nom>". Si no passes cap nom, ha de imprimir "Hola, amic".
# Autor: Biel Rull Simon

nom = "amic"

def saluda_nom(nom):
    print("Hola", nom)
    return
saluda_nom("Joan")
saluda_nom(nom)
saluda_nom("Laia")