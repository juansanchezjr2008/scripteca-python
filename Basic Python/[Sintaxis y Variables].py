'''
¿Ves esto?, esto es un comentario multilinea, a continuacion te mostraré
uno basico. este esta entre 6 comillas simples, lo escrito aqui no se mostrara
en consola u alguna otra salida, y el multilinea te permite hacer comentarios
muchisimo más detallados con saltos de linea posibles.
'''

# Esto es un comentario basico, y se me esta acabando el espacio... aaaaah!
# Asi que tuve que usar otro, los comentarios son para ti o para tus compañeros del proyecto.

'''
Tu determinas cuales usar, dependiendo lo que necesites en el momento,
ejemplo, a comtinuacion los usare mixtos para explicarte como funcionan esos
datos que se reflejaran en la salida, como las variables...
'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# 1. Print y su sintaxis.

print('Print, funciona para mostrar datos en consola, esta es su sintaxis.')
# primero se establece la palabra reservada "print" seguido "()" y dentro el texto entre comillas.
# # → Abre la consola para ver este texto impreso.

# 2. Tipos de variable y sintaxis.
# # → La sintaxis es sencilla [Clave] = [Valor], los valores son los que cambian de sintaxis.
# # TIPOS DE VARIABLES:

nombre = 'Juan de Dios' #String: Texto, va estrictamente entre comillas simples o dobles
edad = 17 #Integer: Numeros Enteros, estos no necesitan comillas.
promedio = 8.5 #Float: Numeros Decimales, requieren el punto, no hace falta explicarlo
casado = False #Boolean: Verdadero o Falso, palabras reservadas "True/False" no necesita comillas.
inicial = 'J' #Char: Rara vez usado, solo admite como texto 1 caracter.
hermanos = ['Eliseo', 'Manuel', 'Ezequiel', 'Moises'] # Arrays: Listas dentro de '[]' admiten varios tipos antes vistos.
jergas = {
    '¿donde estas?' : 'ontas?',
    'sorprendente' : '¡El diablo!',
    'vete de aqui' : '¡Abrete!',
    'Una quina' : 500
} #Dictionary: Diccionarios, dentro de "{}" formando pares de valores semejantes o mixtos con ":" y separados por comas.

# 3. Imprimiendo las variables:
# → si solo te interesa mostrar una, puedes pasarla dentro de los "()", sin necesidad de las comillas.

print(nombre) # muestra en consola "Juan de Dios"

# → para unirla con más texto podria valer de mixtos entre textos y variables separados por comas.

print('Mi nombre es ', nombre, 'y tengo ', edad) # esto muestra "Mi nombre es Juan de Dios y tengo 17".

# 4. Variables en espera de datos:
# → Estas variables son dinamicas y estan en espera de "Input" el cual almacena texto, nueva palabra reservada.

intereses = input('Ingresa tus intereses de hoy: ') # esto muestra el la descripcion del campo y la variable valdra lo ingresado
print(intereses)