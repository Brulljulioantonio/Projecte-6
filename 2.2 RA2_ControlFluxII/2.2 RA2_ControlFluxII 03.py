# Què fa el programa: mostra la taula de multiplicar del número que l'usuari introdueix
# Autor: Biel Rull Simon
# Data:  8/10/25

# Versió 1.0

nummult = int(input("taula del... "))
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(nummult, "x" ,i, "=", nummult * i)