"""
	Ejercicio1: Practica de uso de Funcion Lambda
	@SantiagoDGarcia

"""
# Se asigna una cadena a la funcion y se transforma a mayusculas en el mismp
cadena_personalizada = lambda x,y: ("%s capital de %s" % (x.upper(),y.upper()))
# Se imprime la cadena con la funcion 
print(cadena_personalizada("Cuenca", "Azuay"))