#EJERCICIO 9
#FECHA: 05/26/2023

año = int(input('Año: '))

if año < 1582:
    print('No dentro del período del calendario Gregoriano.')
elif not año % 4:
    print('Es un año bisiesto')
elif not año % 100:
    print('Es un año comun')
elif not año % 400:
    print('Es un año bisiesto')
else:
    print('Es un año comun')     