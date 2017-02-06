#  APUNTES LIBRERÍA ITERTOOLS 
#http://python-para-impacientes.blogspot.com.es/2015/08/bucles-eficientes-con-itertools.html

# FUNCIONES QUE DEVUELVEN ITERABLES INFINITOS:

''' itertools.count(start=0 [, step=1])
	Devuelve iterable ininterrumpido '''

	from itertools import *
	for valor in count(5, 3):
	    print(valor, end = ' ')
	    if valor == 20: break
	# Salida: 5 8 11 14 17 20

''' itertools.cycle(iterable)
	Devuleve un iterable ininterrumpido dándole otro iterable de entrada'''

	# cycle() con una cadena:
	contador = 0
	for elemento in cycle("Python"):
	    print(elemento, end = ' ')
	    contador += 1
	    if contador == 12: break
	# Salida: P y t h o n P y t h o n

	#cycle() con una lista:
	contador = 0
	for elemento in cycle([10, 12, 14]):
	    print(elemento, end = ' ')
	    contador += 1
	    if contador == 5: break
	#Salida: 10 12 14 10 12 

	# cycle() con un diccionario:
	contador = 0
	for elemento in cycle({'x':1, 'y':2, 'z': 3}):
	    print(elemento, end = ' ')
	    contador += 1
	    if contador == 9: break
	#Salida: x z y x z y x z y 

''' itertools.repeat(object[, times])
	devuelve el objeto repetido una y otra vez indefinidamente a no ser que se especifique en times.'''
	# repeat() con un entero:
	for elemento in repeat(3, 5):
	    print(elemento, end = ' ')
	#Salida: 3 3 3 3 3

	# repeat() con map():
	print(list(map(pow, range(5), repeat(3))))
	#Salida: [0, 1, 8, 27, 64] 

# FUNCIONES QUE DEVUELVEN ITERABLES QUE FINALIZAN:

'''itertools.accumulate(iterable[, func])
	Devuelve iterable con sumas acumuladas o derivadas de una función'''

	# accumulate() con la función implícita que acumula sumas: 
	for acumulado in accumulate([1, 2, 3, 4, 5]):
	    print(acumulado, end = ' ')
	# Salida: 1 3 6 10 15

	# accumulate() con función max para 'acumular' el valor máximo:
	for valor_maximo in accumulate([1, 3, 2, 5, 4], max):
	    print(valor_maximo, end = ' ')
	# Salida: 1 3 3 5 5

	# acumulate() con función lambda:
	for diferencia in accumulate([10, 30, 50], lambda a, b: b-a):
	    print(diferencia, end = ' ')
	# Salida: 10 20 30 

''' itertools.chain(*iterables)