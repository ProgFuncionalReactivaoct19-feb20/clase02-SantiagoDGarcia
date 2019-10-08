"""
	Ejercicio1: Ejemplo de uso de Funcion Lambda
	@SantiagoDGarcia
"""

tupla = (
		 (100, 170),
		 (200, 180)
		)

funYear = lambda x: x[0]
funEstatura = lambda x: x[1]

funciones = lambda x:(funYear(x)/12.0, funEstatura(x)/100)
print(list(map(funciones, tupla)))