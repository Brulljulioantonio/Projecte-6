# Què fa el programa: Crea un programa que escrigui les següents 3 línies en un fitxer nou anomenat sortida.txt. El contingut anterior (si n'hi ha) ha de desaparèixer.
# Autor: Biel Rull Simon

fitxer = open("/workspaces/Projecte-6/2.6 RA2_Fitxers/2.6 RA2_Fitxers 02/sortida.txt", "w")
fitxer.write("primera linea\n")
fitxer.write("segona linea\n")
fitxer.write("tercera linea\n")

fitxer = open("sortida.txt", "r")
print(fitxer.read())
fitxer.close()