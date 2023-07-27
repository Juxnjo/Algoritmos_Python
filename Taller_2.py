#TALLER 2 PYTHON
#FECHA: 05/04/2023

a=int(input('Digite un numero '))
b=int(input('Digite otro numero '))
c=int(input('Digite un tercer numero '))
x= [a,b,c]
print('El valor maximo es ', max(x))
print('El valor minimo es', min(x))
print('La suma de los valores es', sum(x))

z=float(input('Ingrese un valor decimal '))
redondear=round(z)
print('El valor con decimal es ',z, 'El valor redondeado es ', redondear)

frase=str(input('Escriba una frase '))
print('La frase en mayuscula es ', frase.upper())
print('La frase en miniscula es ', frase.lower())
print('La primera en mayuscula es ', frase.capitalize())
print('La frase con palabras en mayuscula es ', frase.title())
print('La longitud de la frase es ', len(frase), 'caracteres')