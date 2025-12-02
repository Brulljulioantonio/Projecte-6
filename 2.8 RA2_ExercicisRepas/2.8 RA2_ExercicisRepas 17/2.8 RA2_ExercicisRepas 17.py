# Què fa el programa:
# Autor: Biel Rull Simon

frase = input("Introdueix una frase a guardar dins de frase.txt ")

fitxer = open("/workspaces/Projecte-6/2.8 RA2_ExercicisRepas/2.8 RA2_ExercicisRepas 17/frase.txt", "w")
fitxer.write(frase)
fitxer.close