#EJERCICIO 10
#FECHA: 05/2/2023

import random

secret_number = random.randint(1,5)
numero = int(input('Ingrese un numero entre 1 y 5: '))

while numero != secret_number:
    print("¡Ja, ja!\n¡Estás atrapado en mi bucle!")
    numero = int(input('Intente nuevamente: '))
    
else:
    numero == secret_number
    print("¡Bien hecho, muggle!\nEres libre ahora")
    

        
    

