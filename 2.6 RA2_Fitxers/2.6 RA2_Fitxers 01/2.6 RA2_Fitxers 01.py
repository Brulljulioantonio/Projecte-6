# Què fa el programa: Crea un fitxer de text anomenat missatge.txt amb contingut a mà (o des del codi). Escriu un programa que llegeixi i mostri el contingut per pantalla.
# Autor: Biel Rull Simon

fitxer = open("/workspaces/Projecte-6/2.6 RA2_Fitxers/2.6 RA2_Fitxers 01/fitxer.txt", "r")
print(fitxer.read())
fitxer.close()