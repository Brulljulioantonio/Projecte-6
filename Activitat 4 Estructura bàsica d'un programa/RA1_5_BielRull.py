# Què fa el programa: Calcula el volum d'una esfera
# Autor: Biel Rull Simon
# Data: 23/09/25

# Versió 1.0

PI = 3.1416 # Constant PI
radi = float(input("Radi? ")) # Variable que asigna l'usuari

def volum_esfera(r): # Funció que calcula el volum d'una esfera
    return (4/3) * PI * r**3

volum = volum_esfera(radi)

print("el volum es: ",volum) # Sortida