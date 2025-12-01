# Què fa el programa:
# Autor: Biel Rull Simon

def major(a, b):
    if a > b:
        return(a, "és mes gran")
    elif a < b:
        return(b, "és mes gran")
    else:
        return("son iguals")
    
print(major(2,45))