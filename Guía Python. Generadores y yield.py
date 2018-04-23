# generadores.
	''' Mediante una sintaxis similar a la comprension de listas devuleve un generador iterable (puede que infinito)
	En lugar de return usa yeld. '''

	def generador(inicio, fin, incremento): # define generador
	    while(inicio <= fin):
	        yield inicio  # devuelve valor y continúa el ciclo (return lo terminaría)
	        inicio += incremento
	 
	for valor in generador(0, 6, 1):  # recorre los valores del generador
	    print(valor)  # muestra valores, uno a uno: 0 1 2 3 4 5 6
	lista = list(generador(0, 8, 2))  # de un generador obtiene una lista
	print(lista)  # muestra lista [0,2,4,6,8]