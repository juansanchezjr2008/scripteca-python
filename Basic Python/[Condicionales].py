'''
En este apartado veremos los condicionales, que son estructuras de control
que permiten ejecutar diferentes bloques de código según ciertas condiciones.
'''

# Condicionales en Python

"""
Las condicionales en Python se implementan utilizando las palabras clave:
- if: para iniciar una condición.
- elif: para agregar condiciones adicionales.
- else: para ejecutar un bloque de código si ninguna de las condiciones anteriores se cumple.

"""

# Ejemplo de condicional simple
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
# En este codigo se verifica si la variable 'edad' es mayor o igual a 18.
# Si es verdadero, se imprime "Eres mayor de edad".

# Ejemplo de condicional con else
edad = 16
if edad >= 18:
    print("Eres mayor de edad")
else: 
    print("Eres menor de edad")
# En este caso, si la condicion no se cumple, se ejecuta el bloque dentro de 'else' el cual imprime "Eres menor de edad".

# Ejemplo de condicional con elif
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muy bien")
elif nota >= 70:
    print("Bien")
else:
    print("Necesitas mejorar")

# Aquí se evalúan varias condiciones. Dependiendo del valor de 'nota', se imprime un mensaje diferente.
# Si 'nota' es 85, se imprimirá "Muy bien".
# Si ninguna de las condiciones se cumple, se ejecuta el bloque dentro de 'else'.
# Es importante notar que Python utiliza la indentación (espacios o tabulaciones) para definir los bloques de código.

# Ejemplo de condicional anidado
numero = 10
if numero > 0:
    print("El número es positivo")
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
else:
    print("El número es negativo o cero")

# En este ejemplo, se verifica si 'numero' es positivo. Si es así, se verifica si es par o impar.
# Si 'numero' no es positivo, se imprime que es negativo o cero.