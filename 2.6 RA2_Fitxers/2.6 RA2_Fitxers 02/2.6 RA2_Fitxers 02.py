# Què fa el programa:
# Autor: Biel Rull Simon

fitxer = open("/workspaces/Projecte-6/2.6 RA2_Fitxers/2.6 RA2_Fitxers 02/sortida.txt", "w", "r")
fitxer.write("primera linea\n")
fitxer.write("segona linea\n")
fitxer.write("tercera linea\n")

print(fitxer.read())
fitxer.close()