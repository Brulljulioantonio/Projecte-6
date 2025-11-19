# Què fa el programa: Afegir continguts: Afegeix una línia nova a un fitxer existent (sortida.txt) sense esborrar el que ja hi ha.
# Autor: Biel Rull Simon

fitxer = open("/workspaces/Projecte-6/2.6 RA2_Fitxers/2.6 RA2_Fitxers 03/sortida.txt", "a")
fitxer.write("nova linea\n")
fitxer.close()