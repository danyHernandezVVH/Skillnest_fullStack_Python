# 🔹 Tipos de datos primitivos
# Estos son los elementos básicos de un lenguaje. La mayoría de
# los lenguajes comparten estos en común.

# 🔘 Booleanos: Se utiliza para representar valores de 
# verdad en la lógica. Solamente puede tener dos valores: 
# True o False (Nota que ponemos la T y la F en mayúsculas).

mayor_edad = True
tiene_bigote = False
# 🔢 Números: Aquí podemos tener números enteros, 
# de punto flotante (también conocidos como números decimales) 
# o complejos.

mayoria_edad = 18
altura = 1.72

# 🔤 Strings: También conocidas como cadenas, se refiere a textos 
# o cadenas de caracteres.

frase = "Anita lava la tina"

# 🧩 Tipos de datos compuestos
# Estas con colecciones compuestas de los datos primitivos 
# vistos anteriormente.

# 📋 Listas: Tipo de datos mutable (que puede cambiar) y
# contiene un conjunto de distintos valores. Suele utilizarse 
# para almacenar información relacionada.

lista_vacia = []  # [] ---> Arreglo o lista (Array)
gatos = ["Garfield", "Silvestre", "Hello Kitty"]
print(gatos[2]) # Imprime: Hello Kitty
gatos[1] = "Tom" # Modificar el valor 1
gatos.append("Felix") #Añade un nuevo valor al final de la lista

print(gatos) #Imprime: ['Garfield', 'Tom', 'Hello Kitty', 'Felix']
gatos.pop() #Elimina el último valor de la lista
# print(gatos) #Imprime: ['Garfield', 'Tom', 'Hello Kitty']

gatos.pop(1) # Elimina el valor en la posición 1 de la lista
print(gatos) #Imprime: ['Garfield', 'Hello Kitty']

# Matrices o Arreglos multidemensiónales: Son listas que 
# contienen otras listas.

Ejemplo_matriz = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]
print(Ejemplo_matriz[1][2]) #Imprime: 6
# Imprimir el numero 9
print(Ejemplo_matriz[2][2]) #Imprime: 9

# Tarea
# Crear una matriz de 4x4 y mostrar el número 16 en la terminal.
matriz_4X4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8], 
    [9, 10, 11, 12],
    [13, 14, 15, 16]
    ]
print(matriz_4X4[3][3]) #Imprime: 16

# 🔒 Tuplas: Tipo de datos inmutable (que no se puede modificar)
# y contiene un conjunto de distintos valores. Pueden contener 
# distintos tipos de datos.
# ejemplo = ("Lunes", "Martes") ---> Paréntesis = Tuplas

perro = ("Scooby Doo", "Gran Danés", "Scooby Galletas", 7)
print(perro[0]) #Imprime: Scooby Doo
# perro[2] = "comida de perro" #ERROR: Las tuplas no pueden 
# ser modificadas (TypeError: 'tuple' object does not support 
# item assignment)

# 🗂️ Diccionarios: Nos permite almacenar contenido a 
# través de una llave y un valor. Podemos acceder a sus datos 
# a través de su índice único (que en este caso llamaremos 
# llave o clave). Encuentra algunos métodos integrados de los 
# diccionarios aquí.

# diccionario_vacio = {} 
# forma de alamacenar datos en un diccionario: {'llave': 'valor'}
# JSON --> es un tipo de dato que se utiliza 
# para almacenar información en un formato de texto plano. 
# Es muy utilizado en la web para intercambiar información 
# entre el cliente y el servidor.

persona = {
    'nombre': 'Carmen', 
    'edad': 31, 
    'altura': 1.71, 
    'usa_lentes': False
    }
persona['nombre'] = 'Valeria'  # Actualiza si el valor de la llave existente
persona['hobbies'] = ['jugar videojuegos', 'programación'] 
#Incorporar nuevas llaves a persona. 
# Profesión, comida favorita, mascotas, peliculas_favoritas.
persona['profesion'] = 'Ingeniera de software'
persona['comida_favorita'] = 'Pizza'
persona['mascotas'] = ['Firulais', 'Mishi']
persona['peliculas_favoritas'] = ['El Padrino', 'Naruto Shippuden']

#imprimir el diccionario completo
print(persona) 

#  Imprime: {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']}
altura = persona.pop('altura')  # Elimina la clave indicada y devuelve el valor
print(altura)    # Imprime: 1.71
print(persona) 

# # salida: {'nombre': 'Carmen', 'edad': 31, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']} 

# ⚙️ Funciones comunes
# En caso de no conocer el tipo de dato de una variable o valor, 
# gracias a la función type podemos saberlo fácilmente. 

# Por ejemplo:
print(type(3.1416)) #Imprime: <class 'float'> --> type
print(type(persona)) #Imprime <class 'dict'>
# En tipos de datos que tienen tamaño 
# (por ejemplo: listas, tuplas, diccionarios, cadenas), 
# podemos usar la función len, que es diminutivo de
# length (tamaño en español) y que nos regresa la 
# longitud de este.

print(len(persona)) #Imprime: 8 (la cantidad de pares de clave-valor)
print(len("Me encanta programar")) #Imprime: 20
