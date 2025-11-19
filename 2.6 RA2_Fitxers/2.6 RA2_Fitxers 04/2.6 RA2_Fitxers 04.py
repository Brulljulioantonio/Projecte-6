# Què fa el programa: Afegir continguts: Llegeix un fitxer i mostra quantes línies té.
# Autor: Biel Rull Simon

fitxer = open("/workspaces/Projecte-6/2.6 RA2_Fitxers/2.6 RA2_Fitxers 04/sortida.txt", "r")
print(len(fitxer.readlines()), "línies")
fitxer.close()