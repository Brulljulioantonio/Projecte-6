# Què fa el programa: Simula una operació amb fitxers on pot haver-hi un error durant la lectura. Assegura’t que el fitxer es tanqui sempre, fins i tot si es produeix un error en llegir-lo. Pista: utilitza try-finally o millor encara: comprova què passa si no utilitzes with i ho fas tot manualment amb .open() i .close().
# Autor: Biel Rull Simon

try:
    fitxer = open("/workspaces/Projecte-6/2.6 RA2_Fitxers/2.6 RA2_Fitxers 10/prova.txt", "r")
    print(fitxer.read())
finally:
    fitxer.close()
    print("El fitxer s'ha tancat correctament.")