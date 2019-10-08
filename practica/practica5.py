"""
	Ejercicio1: Practica de uso de Funcion Lambda
	@SantiagoDGarcia

"""
datos = [(10,2), (8,7), (5,4), (3,11), (10,11)]
# Se reduce la lista a sus tuplas para determinar sus términos
reduccion = lambda x: x[0]
raiz = lambda x: x[0]**0.5
# Se establece el print de la primera funcion el cual pide la raiz del primer termino
print(list(map(raiz, datos)))

# Se establece la 2da funcion a usar, la potencia, la que se requiere del segundo termino
potencia = lambda x: x[1]**2
print(list(map(potencia, datos)))