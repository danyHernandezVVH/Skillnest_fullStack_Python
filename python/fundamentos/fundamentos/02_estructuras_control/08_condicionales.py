#Condicionales
#Estructura else - if
num = 15
if num > 20:
    print("Número mayor a 20")
else:
   print("Número menor a 20")
'''
La variable num es menor a 20, por lo que el bloque de código 
de else será ejecutado.
Es decir que vamos a imprimir "Número menor a 20"
'''
#Estructura if - elif - else
num = 101
if num > 50:
   print("Número mayor a 50")
elif num > 100:
   print("Número mayor a 100")
else:
   print("Número menor a 10")
'''
A pesar de que num es mayor que 50 y 100, la primera condicional 
que se cumpla es la única que se ejecutará.
Es por eso que solo imprimirá: "Número mayor a 50"
'''
if num < 60:
   print("Número menor a 50") #Nunca entramos a esta línea de código

#No se cumple con la condicional, por lo que no se ejecuta el bloque de código

#Tarea desafío
#Ingresar 3 números por teclado e identificar cual es el mayor y cual
# es el menor. Mostrar ambos.
n1 = int(input("Ingresar primer número: "))
n2 = int(input("Ingresar segundo número: "))
n3 = int(input("Ingresar tercer número: "))

#Estructura if - elif - else
if n1 >= n2 and n1 >= n3:
    mayor = n1
    if n2 <= n3:
      menor = n2
    else:
       menor = n3
elif n2 >= n1 and n2 >= n3:
    mayor = n2
    if n1 <= n3:
      menor = n1
    else:
       menor = n3
else:
    mayor = n3
    if n1 <= n2:
        menor = n1
    else: 
        menor = n2
print(f"El mayor es {mayor} y el menor es {menor}")
    
      

      


'''
#Detectar menor
if num1 == num2 and num1 == num3:
   print("Todos los números son iguales")
elif num1 < num2 and num1 < num3:
   print(f"El número {num1} es menor que {num2} y {num3}")
elif num2 < num1 and num2 < num3:
   print(f"El número {num2} es menor que {num1} y {num3}")
elif num3 < num1 and num3 < num2:
   print(f"El número {num3} es menor que {num1} y {num2}")
else:
   print("Ingrese valores válidos")
#Detectar mayor (lo mismo pero cambiando < por >)
if num1 == num2 and num1 == num3:
   print("Todos los números son iguales")
elif num1 > num2 and num1 > num3:
   print(f"El número {num1} es mayor que {num2} y {num3}")
elif num2 > num1 and num2 > num3:
   print(f"El número {num2} es mayor que {num1} y {num3}")
elif num3 > num1 and num3 > num2:
   print(f"El número {num3} es mayor que {num1} y {num2}")
else:
   print("Ingrese valores válidos")



mayor = num1
if num2 > mayor:
    mayor = num3 
if num3 > mayor :
   mayor = num3

   print("el numero mayor es ", mayor)

menor = num1
if num2 < menor:
    mayor = num3 
if num3 < menor :
   mayor = num3

   print("el numero menor es ", menor)
'''
   #camilo +1