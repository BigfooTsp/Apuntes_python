PROGRAMACIÓN FUNCIONAL I. Funciones de orden superior:

	'''Enfoque más matemático que la programación imperativa

	http://python-para-impacientes.blogspot.com.es/2014/02/programacion-funcional-funciones-de.html '''

# map(función, iterable) Aplica una función a una lista de datos y devuelve un iterable.
	def cuadrado(numero):       
	    return numero ** 2
	 
	lista1 = [-2, 4, -6, 8]
	lista2= list(map(cuadrado, lista1))  # devuelve un iterador que convertimos a lista
	print(lista2)  # resultado: 4, 16, 36, 64

	#O con un for
	for resultado in map(cuadrado, lista2): 
    print(resultado)

# filter(función filtro, iterador) Aplica filtro a lista de datos y devuelve iterados con los datos encontrados.
	def esneg(numero):  # esneg() se aplicará a todos los número de lista  
	    return (numero < 0)  # devuelve True o False según sea un nº negativo o no
	 
	lista5 = [-3, -2, 0, 1, 9, -5]
	print(list(filter(esneg, lista5)))  # devuelve los números negativos de la lista

# reduce(función, lista) aplica la función a una lista por pares, empezando por los dos primeros, 
	''' dejando al final solo un elemento. 
	Para utilizarlo a partir de python 3 se debe importar módulo functools. '''
	import functools
	 
	def multiplicar(x, y):
	    print(x * y)  # muestra el resultado parcial
	    return x * y
	 
	lista = [1, 2, 3, 4]
	valor = functools.reduce(multiplicar, lista)
	print(valor)  # muestra el resultado final

# x = lambda variable:func	Declara funciones de una sola linea que asigna a variables.
	cuadrado = lambda x: x*x
	 
	lista = [1,2,3,5,8,13]
	for elemento in lista: 
	    print(cuadrado(elemento))

