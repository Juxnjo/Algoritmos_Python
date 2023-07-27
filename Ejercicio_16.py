#EJERCICIO 16
#FECHA: 06/06/2023


beatles = []
print("Lista vacia ", beatles)
beatles.append(["John Lennon", "Paul McCartney", "George harrison"])
print("Agregando a la lista vacia ", beatles)

for beatles in beatles:
    beatles.append(["Stu Sutcliffe", "Pete Best"])
    print("Agregando lista a la lista ", beatles)
    del beatles[3]
    print("Eliminando la lista de la lista ", beatles)
    beatles.insert(0,"Ringo Starr")
    print("Agregando a la posicion 0 de la lista ", beatles)

