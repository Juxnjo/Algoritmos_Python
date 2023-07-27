#EJERCICIO 8
#FECHA: 05/22/2023

ingreso = float(input('Cuanto son sus ingresos anuales '))

if ingreso < 85528:
    impuesto = round((ingreso*0.18)-556.02)
    
else:
    excedente = ingreso - 85528
    impuesto = round(14839.02 + excedente * 0.32)
    
if impuesto < 0:
    impuesto = 0

print('El impuesto es ', impuesto)