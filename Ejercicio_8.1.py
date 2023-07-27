ingreso = float(input("Ingrese sus ingresos: "))

if ingreso < 85528:
    print("Su impuesto es igual a: ",(ingreso * 0.18) - 556.02)
    
elif ingreso >= 85528:
    excedente = ingreso - 85528
    print("Su impusesto es igual a: ",(14839.02 + excedente * 0.32 ))
    
if  ingreso < 0:
    ingreso = 0
    print("Su impuesto es igual a: ", ingreso)
