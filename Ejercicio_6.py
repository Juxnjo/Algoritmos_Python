#EJERCICIO 6
#FECHA: 05/22/2023

hora = 3
min = 10
duracion = 70

minutos = (min + duracion)%60
horas = int (hora  +((min + duracion)/60))%24

print(horas,':', minutos)