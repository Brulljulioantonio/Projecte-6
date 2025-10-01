# Què fa el programa: comprova si ets major d'edat o no
# Autor: Biel Rull Simon
# Data: 1/10/25

# Versió 1.0

data_A = int(input("any actual? "))
data_N = int(input("introdueix la data de naixement: "))

if (data_A - data_N) >= 18:
    print("major d'edat")
if(data_A - data_N) < 18:
    print("menor d'edat")