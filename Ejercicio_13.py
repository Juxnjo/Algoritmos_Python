#EJERCICIO 13
#FECHA: 05/27/2023

vocales = ['A', 'E', 'I', 'O', 'U']
palabra = str(input('Ingrese una palabra: '))
palabra = palabra.upper()

for letra in palabra:
    if letra in vocales:
        continue
    print(letra)

