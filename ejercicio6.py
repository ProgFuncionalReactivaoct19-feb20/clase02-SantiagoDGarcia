"""
	Ejercicio1: Ejemplo de uso de Funcion Lambda
	@SantiagoDGarcia
"""
lista = [10, 2, 3, 5, 1]

funYear = lambda x: x[0]
funEstatura = lambda x: x[1]

funciones = lambda x: x+100
print(min(list(map(funciones, lista))))