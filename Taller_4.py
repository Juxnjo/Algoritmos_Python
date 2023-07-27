#TALLER 4 PYTHON
#FECHA: 05/22/2023

print('EJERCICIO DE LAS CLASES DE TRIANGULOS')
a = int(input('digite el valor de A: '))
b = int(input('digite el valor de B: '))
c = int(input('digite el valor de C: '))

if a == b and a == c and b == c:
    print('El triangulo es equilatero')
else:
    if a == b or b == c or a == c:
        print('El triangulo es isoceles')
    else:
        print('el tiangulo es escaleno')
print()
animal=input('digite un animal ')
animal = animal.upper()
if animal == 'PERRO':
    print('Este animal es el mejor amigo del hombre ', animal)
elif animal == 'GATO':
    print('Este animal persigue a los ratones ', animal)
elif animal == 'OSO':
    print('Este animal vive en el bosque ', animal)
else:
    print('No es PERRO, no es GATO, ni es OSO... es: ', animal)
