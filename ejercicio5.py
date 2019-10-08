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
# Se usa primeramente la fun Dato para encontrar la 3ra poscicion dentro de la tupla
# Luego se usa la 2da funcion para encontrar la 1ra poscion dentro de la tupla anterior seleccionada

funciones = lambda x:(funYear(x)/12.0, funEstatura(x)/100)
print(list(map(funciones, tupla)))