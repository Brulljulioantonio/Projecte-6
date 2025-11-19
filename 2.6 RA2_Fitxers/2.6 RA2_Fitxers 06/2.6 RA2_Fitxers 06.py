# Què fa el programa: Fes un programa que intenti llegir un fitxer anomenat dades.txt, però abans comprovi si existeix. Si no existeix, mostra un missatge d’error amigable.
# Autor: Biel Rull Simon

fitxer = open("/workspaces/Projecte-6/2.6 RA2_Fitxers/2.6 RA2_Fitxers 06/dades.txt", "r")
print(fitxer.read())
fitxer.close()