PROGRAMACIÓN FUNCIONAL II. Funciones de orden superior:
		
	'''Enfoque más matemático que la programación imperativa

	http://python-para-impacientes.blogspot.com.es/2014/02/programacion-funcional-funciones-de.html '''

# Comprensión de listas.
	''' Tipo de construcción que mediante una expresión modifica un iterable usando sentencias
	for e if obteniendo otro iterable. '''
	lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	cubos = [valor ** 3 for valor in lista]  # cada elemento de la lista se eleva al cubo
	print('Cubos de 1 a 10:', cubos)
	 
	numeros = [135, 154, 180, 193, 210]
	divisiblespor3 = [valor for valor in numeros if valor % 3.0 == 0] 
	print(divisiblespor3)  # muestra lista con los números divisibles por 3
	 
	def funcion(x):  # define función
	    return 1/x  # devuelve inverso de un número
	 
	L = [1, 2, 3]  # declara lista
	print([funcion(i) for i in L])  # muestra lista con inversos de cada número

# generadores.
	''' Mediante una sintaxis similar a la comprension de listas devuleve un generador iterable (puede que infinito)
	En lugar de return usa yeld. '''

	def generador(inicio, fin, incremento): # define generador
	    while(inicio <= fin):
	        yield inicio  # devuelve valor
	        inicio += incremento
	 
	for valor in generador(0, 6, 1):  # recorre los valores del generador
	    print(valor)  # muestra valores, uno a uno: 0 1 2 3 4 5 6
	lista = list(generador(0, 8, 2))  # de un generador obtiene una lista
	print(lista)  # muestra lista [0,2,4,6,8]

# Decoradores: Funciones que reciben una función como parámetro y devuelve otra función.
	def decorador1(funcion):
	    def funciondecorada(*param1, **param2):
	        print('Inicio', funcion.__name__)
	        funcion(*param1, **param2)
	        print('Fin', funcion.__name__)
	    return funciondecorada
	     
	def suma(a, b):
	    print(a + b)
	 
	suma2 = decorador1(suma)
	suma2(1,2)
	suma3 = decorador1(suma)
	suma3(2,2)
	 
	# Otra forma más elegante, usando @:
	 
	@decorador1
	def producto(arg1, arg2):
	    print(arg1 * arg2)
	 
	producto(5,5)