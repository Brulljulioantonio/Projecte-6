# Què fa el programa: Fes un programa que mostri la data i hora actual i la formati de manera llegible.
# Autor: Biel Rull Simon

import datetime

data_hora_actual = datetime.datetime.now()
data_hora_formatada = data_hora_actual.strftime("%d/%m/%Y %H:%M:%S")
print("Data i hora actual:", data_hora_formatada)