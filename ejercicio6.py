"""
	Ejercicio1: Ejemplo de uso de Funcion Lambda
	@SantiagoDGarcia
"""
lista = [10, 2, 3, 5, 1]

funYear = lambda x: x[0]
funEstatura = lambda x: x[1]
# Se usa primeramente la fun Dato para encontrar la 3ra poscicion dentro de la tupla
# Luego se usa la 2da funcion para encontrar la 1ra poscion dentro de la tupla anterior seleccionada

funciones = lambda x: x+100
print(min(list(map(funciones, lista))))