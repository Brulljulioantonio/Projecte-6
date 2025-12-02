# Què fa el programa:
# Autor: Biel Rull Simon

fitxer = open("/workspaces/Projecte-6/2.8 RA2_ExercicisRepas/2.8 RA2_ExercicisRepas 19/fitxer.txt", "r")
contador = 0

for i in fitxer:
    contador += 1
print("Hi han", contador, "linees")