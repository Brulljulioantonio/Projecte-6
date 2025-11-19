# Què fa el programa: Escriu un programa que intenti escriure en un fitxer anomenat resultats.txt, però gestiona l'error que es pot produir si el fitxer és només de lectura o si el sistema impedeix escriure-hi (permisos denegats).
# Autor: Biel Rull Simon

try:
    fitxer = open("/workspaces/Projecte-6/2.6 RA2_Fitxers/2.6 RA2_Fitxers 07/resultats.txt", "w")
    fitxer.write("Aquest és un nou resultat.\n")
    fitxer.close()
except PermissionError:
    print("Error: No tens permisos per escriure en el fitxer resultats.txt.")