# Què fa el programa: Obre un fitxer en mode lectura i escriptura (r+). Mostra el contingut per pantalla i afegeix una línia al final sense esborrar el contingut anterior.
# Autor: Biel Rull Simon

fitxer = open("/workspaces/Projecte-6/2.6 RA2_Fitxers/2.6 RA2_Fitxers 05/sortida.txt", "r+")
print(fitxer.read())
fitxer.write("nova linea\n")
fitxer.close()