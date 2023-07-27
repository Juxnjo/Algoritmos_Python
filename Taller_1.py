#TALLER 1 PYTHON
#FECHA: 05/04/2023

from datetime import date #importar fecha
hoy = date.today()
print('Hoy es el dia: ', hoy)

n1=int(input('Ingrese un numero '))
n2=int(input('Ingrese otro numero '))
sumar=n1+n2
print('La total de la suma es ', sumar)
restar=n1-n2
print('El total de la resta es ', restar)
multiplicar=n1*n2
print('El total de la multiplicacion es ', multiplicar)
division=n1//n2 #La // es para quitar el decimal a la division
print('El total de la division es ', division)

