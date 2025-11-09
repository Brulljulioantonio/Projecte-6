# Què fa el programa: Fes un programa que mostri la data i hora actual i la formati de manera llegible.
# Calcula quants dies falten per una data determinada (com Nadal o el teu aniversari).
# Autor: Biel Rull Simon

import datetime

data_hora_actual = datetime.datetime.now()
data_hora_formatada = data_hora_actual.strftime("%d/%m/%Y %H:%M:%S")
print("Data i hora actual:", data_hora_formatada)

data_objectiu = datetime.datetime(data_hora_actual.year, 12, 25)
if data_hora_actual > data_objectiu:
    data_objectiu = data_objectiu.replace(year=data_hora_actual.year + 1)
dies_faltants = (data_objectiu - data_hora_actual).days
print("Dies fins Nadal:", dies_faltants)