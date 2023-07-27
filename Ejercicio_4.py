#EJERCICIO 4
#FECHA: 05/22/2023

def mi_a_km(millas):
    km = millas * 1.61
    return km

def km_a_mi(km):
    millas = km / 1.61
    return millas

millas = float(input('Ingrese las millas: '))
km = mi_a_km(millas)
print(millas, 'millas son', km, 'kilometros')

km = float(input('Ingrese los kilometros: ')) 
millas = km_a_mi(km)
print(km, 'kilometros son', millas, 'millas')
