# Què fa el programa: Escriu una funció factorial(n) que calculi el factorial d'un nombre n de forma recursiva. 
# (Pista: factorial de n és n * factorial(n-1), amb factorial(0) = 1.)
# Autor: Biel Rull Simon

# Descomentar linies 6 i 13 per provar amb un número introduït per l'usuari
# num = int(input("Introdueix un número enter "))

def factorial(num):
    resultat = 1
    for i in range(1, num + 1):
        resultat *= i
    return resultat
# print(factorial(num))
print(factorial(0))
print(factorial(3))
print(factorial(5))