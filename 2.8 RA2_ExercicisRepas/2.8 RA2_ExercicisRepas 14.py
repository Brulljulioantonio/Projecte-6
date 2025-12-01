# Què fa el programa:
# Autor: Biel Rull Simon

def mitjana(a):

    contador = 0
    total = 0
    
    for i in a:
        contador += 1
        total += i
    return(total / contador)
    
print(mitjana([1,2,3,4,5,6,7,8,9,10]))