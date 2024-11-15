
### Ejercicio 4 
Paises1 = input('Introduzca su primer pais')
Paises2 = input('Introduzca su segunda pais')
Paises3 = input('Introduzca su tercer pais')
Paises_completos = [Paises1, Paises2, Paises3]
print ('Me gustaria visitar',Paises_completos[0])
print ('Me gustaria visitar',Paises_completos[1])
print ('Me gustaria visitar',Paises_completos[2])
### Lista Numeros enteros maximo y minimo
import math
Numeros = input('Introduzca numeros enteros separados por ,')
Numeros1 = [int(num) for num in Numeros.split(',')]
print ('Este es el numero mas alto de la lista',(max(Numeros1)))
print ('Este es el numero mas bajo de la lista',(min(Numeros1)))
'''Realizamos una variable donde introducimos x numeros separados por coma
luego los pasamos a una lista separados por coma 
y printeamos el numero mas alto y mas bajo'''