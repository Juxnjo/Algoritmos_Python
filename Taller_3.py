#TALLER 3 PYTHON
#FECHA: 05/17/2023

from datetime import date
hoy = date.today() 
print ("Hoy es el día: ", hoy)

a=int (input ("digite el valor de A: "))
b=int (input ("digite el valor de B: "))

if a >=b:
    print ("A es mayor o igual a B")
else:
    print ("A es menor que B")
print()
curso1="Requerimientos"
curso2="Algoritmos"
print ("El curso1 es: ", curso1)
print("El curso2 es: ", curso2)
if curso1 == "Requerimientos" and curso2 == "Algoritmos":
    print ("Usted estudia Programación de Software")
else:
    print ("Usted estudia otro programa diferente a Programación de Software")
print()
print ('*** Final del analisis del programa de formacion Sena ***')
print()
frase=input ("digite una oracion: ")
print("La frase en mayuscula es: ", frase.upper())
longitud=len(frase)
print ("La longitud de la frase es: ", len(frase), "caracteres”")
if longitud>10:
    print ("La frase contiene mas de 10 caracteres")
else:
    print ("La frase contiene menos de 11 caracteres")
print()
print ("FIN")

