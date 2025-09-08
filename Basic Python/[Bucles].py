''' 

En python hay unas estructuras llamadas 'Bucles' las cuales son estructuras de 
control que ejecutan un bloque de codigo multiples veces hasta que se 
le indique que pare.

'''

#Bucle for:
 
'''
Se usa para iterar sobre secuencias como listas, tuplas o cadenas, se ejecuta todo el bloque 
por cada elemento. Tiene dos tipos principales los cuales son "in" y "in range"
'''

'''
Ejemplo de bucle for "in" En este bucle estas recorriendo toda la lista en secuencia
en pocas palabras el codigo significa "Para cada elemento 'fruta' dentro de la lista 'frutas'
haz lo siguiente." 
'''

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Me gusta la", fruta)
#Salida: Me gusta la manzana Me gusta la banana Me gusta la cereza 

''' 
Ejemplo de for "in range" En este otro bucle for usas la funcion 'range' para devolver un objeto
iterable que genera una secuencia de números enteros

Su sintaxis es: 

range(final)
range(inicio, final)
range(inicio, final, incremento)
'''

for i in range(5):
    print(i)
# Salida: 0 1 2 3 4


# Bucle while. 