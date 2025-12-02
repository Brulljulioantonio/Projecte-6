# Què fa el programa:
# Autor: Biel Rull Simon

fitxer = open("/workspaces/Projecte-6/2.8 RA2_ExercicisRepas/2.8 RA2_ExercicisRepas 20/fitxer.txt", "w")
llista_num = list(map( int, input("Introdueix una llista de números separats per espais o comes: ").split()))
suma = 0
nvalors = 0

for i in llista_num:
    suma += i
    nvalors += 1
    mitjana = suma / nvalors

fitxer.write(f"El total es: {suma}\nLa mitjana es: {mitjana}")
fitxer = open("/workspaces/Projecte-6/2.8 RA2_ExercicisRepas/2.8 RA2_ExercicisRepas 20/fitxer.txt", "r")
print(fitxer.read())
fitxer.close