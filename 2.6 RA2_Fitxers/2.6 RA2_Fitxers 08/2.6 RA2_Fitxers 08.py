# Què fa el programa: Suposa que tens un fitxer nombres.txt que hauria de contenir un nombre enter per línia. Fes un programa que llegeixi cada línia i la transformi en enter. Si alguna línia no és un enter vàlid, captura l’error i mostra un missatge, però continua amb la resta.
# Autor: Biel Rull Simon

fitxer = open("/workspaces/Projecte-6/2.6 RA2_Fitxers/2.6 RA2_Fitxers 08/nombres.txt", "r")
for i in fitxer:
    try:
        nombre = int(i)
        print("Nombre llegit: ", nombre)
    except ValueError:
        print("Error: La línia ",i, " no és un enter vàlid.")
fitxer.close()