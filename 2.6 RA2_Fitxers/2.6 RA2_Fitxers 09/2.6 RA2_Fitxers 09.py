# Què fa el programa: Intenta obrir un fitxer en mode lectura. Si no existeix, crea’l automàticament i escriu-hi una línia per defecte: "Fitxer creat automàticament" Pista: utilitza try-except amb open(...) en mode "r", i si falla, obre'l en mode "w".
# Autor: Biel Rull Simon

try:
    fitxer = open("/workspaces/Projecte-6/2.6 RA2_Fitxers/2.6 RA2_Fitxers 09/dades.txt", "r")
    contingut = fitxer.read()
    print("Contingut del fitxer:")
    print(contingut)
    fitxer.close()
except FileNotFoundError:
    fitxer = open("/workspaces/Projecte-6/2.6 RA2_Fitxers/2.6 RA2_Fitxers 09/dades.txt", "w")
    fitxer.write("Fitxer creat automàticament\n")
    fitxer.close()
    print("El fitxer dades.txt no existia i s'ha creat automàticament.")