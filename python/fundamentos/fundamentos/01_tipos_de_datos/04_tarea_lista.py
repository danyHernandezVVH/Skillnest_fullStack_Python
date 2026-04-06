''' Actividad: Gestor de inventario
1.- Creación: Crear una lista llamada inventario que contenga los siguientes
 articulos: "laptop", "ratón", "monitor", "cable hdmi" '''

inventario = ['laptop','ratón','monitor','cable hdmi']

''' 2.- Expansión: Utiliza el método correspondiente para agregar "impresora" 
y "teclado" al final de la lista '''
inventario.append("impresora")
inventario.append("teclado")
# Donovan +1D

''' 3.- Conteo: Utiliza la funcion integrada para mostrar cuantos elementos 
totales hay en la lista.  '''
print(len(inventario))
# Camilo +1D

''' 4.- Acceso y modificación: Modifica "teclado" por "teclado mecánico" '''
inventario[5] = "Teclado mecánico"
print(f"4.- Modificado: {inventario}")
# Arael +1D

''' 5.- Slicing: Crea una nueva lista llamada "promoción", debe contener
solo los 3 primeros elementos de la lista "inventario".  '''
promocion = inventario
print(f"5.- Lista promoción: {promocion[:4]}")
# Camilo +1D

''' 6.- Mostrar la lista de inventario ordenado alfabeticamente.'''
inventario.sort()
print(f"6.- {inventario}") 
# benjamin D +1d

''' 7.- Elimina el último elemento de la lista inventario mostrando el elemento
eliminado y la lista final '''
#benjamin T +1d
eliminado = inventario.pop()
print("Articulo eliminado", eliminado)
print(inventario)