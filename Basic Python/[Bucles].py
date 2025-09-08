''' 

En python hay unas estructuras llamadas 'Bucles' las cuales son estructuras de 
control que ejecutan un bloque de codigo multiples veces hasta que se 
le indique que pare.

'''

# Bucle for in:
 
'''
El bucle for 'in' se utiliza para recorrer elementos de una secuencia 
(listas,cadenas,tuplas,diccionarios,conjuntos rangos, etc)

Su sintaxis es:
for variable in secuencia:

'variable' representa el elemento de la secuencia en cada iteración,
'secuencia' puede ser una lista, tupla, cadena, etc.
'''

# Ejemplo de bucle for "in".

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Me gusta la", fruta)
#Salida: Me gusta la manzana Me gusta la banana Me gusta la cereza 

# Bucle for "in range"

'''
Genera una secuencia de numeros enteros. Es útil para repetir un bloque de codigo un número determinado
de veces.

Su sintaxis es: 
range(final)
range(inicio, final)
range(inicio, final, incremento)
'''

# Bucle for "in range"

for i in range(5):
    print(i)
# Salida: 0 
#         1 
#         2 
#         3 
#         4


# Bucle while. 

'''
El bucle 'while' es una estructura de control que se repite en un bloque de
codigo mientras se cumpla una condicion o hasta que se le indique que pare.
'''

#EJempĺo de bucle While.

contador = 0

while contador < 5:
    print("Contador:", contador)
    contador += 1
#Salida: Contador: 0
#        Contador: 1
#        Contador: 2
#        Contador: 3
#        Contador: 4

# RIESGO

'''
Hay un riesgo en especial con este tipo de bucles el cual es que puedes hacer un 
bucle infinito por una mala sintaxis o que no le indiques que se detenga correctamente.
'''

''' 
Para indicarle que se detenga hay una palabra clave la cual es "break"
permite salir del bucle inmediatamente, incluso si la condicion sigue siendo verdadera.
'''