###lado x lado
def area_cuadrado(lado):
    Area = lado * lado
    print (Area)
    return Area
lado = int(input('Introduce un lado'))
area_cuadrado(lado)
'''Hemos realizado una funcion para realizar el area de un cuadrado
en este caso le pedimos al usuario un lado del cuadrado y dentro de la funcion 
realizamos la operación'''
###Mayor de 3
def mayor_de_tres(a, b, c):
    print (max(a,b,c))
a = int(input('Intrduce tu primer numero'))
b = int(input('Intrduce tu primer numero'))
c = int(input('Intrduce tu primer numero'))
mayor_de_tres(a,b,c)
'''En este caso realizamos una funcion que recoja 3 variables
para comparar cual es el mayor'''