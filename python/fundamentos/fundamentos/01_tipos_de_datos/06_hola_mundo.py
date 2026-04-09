# 1. Imprime "Hola, mundo"
#    Reemplaza el comentario con el código necesario para que, al ejecutar,
#    aparezca en pantalla la frase "Hola, mundo".
#    Ejemplo de uso: print("Mensaje")
# ---------------------------------------------------------------
# (tu código aquí)

print("Hola, Mundo")

# 2. Imprime "Hola, Valeria" con el nombre en una variable
#    a) Concatenación usando comas
#    b) Concatenación usando +
# ---------------------------------------------------------------
nombre = "Valeria"
print("Hola, " + (nombre))
# juan donoso +1
# a) Usando comas
# (tu código aquí)
print("Hola" , nombre)
# b) Usando +
# (tu código aquí)
print("Hola, " + nombre)


# 3. Imprime "Hola 156!" con el número en una variable
#    a) Usando comas
#    b) Usando + (esto podría dar error si no conviertes el número a str)
# ---------------------------------------------------------------
numero = 156
print(f"Hola {numero}")
# a) Usando comas
# (tu código aquí)
saludo = "Hola"
print(saludo , numero)
# b) Usando +
# (tu código aquí)
# BONUS: Corrige el error con conversión de tipos si aparece.
todo = saludo + str(numero)
# Camilo +1

# 4. Imprime "Me encanta comer X e Y" con dos de tus comidas favoritas
#    a) Usando .format()
#    b) Usando f-strings
# ---------------------------------------------------------------
comida1 = "pizza"
comida2 = "hamburguesa"


# a) Con .format()
# (tu código aquí)
print("Me encanta comer {} y {}".format(comida1, comida2))
#tete +1

# b) Con f-string
# (tu código aquí)
print(f"Me encanta comer {comida1} y {comida2}.")
#luis +1


# Desafío bonus: Usa al menos un método de cadena adicional.
# Ejemplo: .upper(), .lower(), .replace(), etc.
# ---------------------------------------------------------------
# (tu código aquí)

nombre = input("Ingresa tu nombre :")
nombre_mayusculas = nombre.upper()
print(nombre_mayusculas)
# Camilo +3