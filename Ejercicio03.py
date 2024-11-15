### Ejercico 3 Numero par o impar
Numero = int(input('Introduzca un numero entero positivo'))
if Numero % 2 == 0:
    print (Numero,'es par')
else:
    print (Numero,'es impar')
### Numero entero lista de multiplos de 3 
Numero_2 = int(input('Introduzca un numero'))
for i in range(0, Numero_2 + 1):
    if i % 3 == 0:
        print (i)