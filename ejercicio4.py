"""
	Ejercicio1: Ejemplo de uso de Funcion Lambda
	@SantiagoDGarcia
"""

tupla = ((30, 1.79), (25, 1.60), (35, 1.68))

funDato = lambda x: x[2]
funEdad = lambda x: x[1]*100
# Se usa primeramente la fun Dato para encontrar la 3ra poscicion dentro de la tupla
# Luego se usa la 2da funcion para encontrar la 1ra poscion dentro de la tupla anterior seleccionada

print(funEdad(funDato(tupla)))