# Crear lista con enteros que son resultados de 
# dos sumas de cuadrados diferentes.

''' Ejercicio que me propuse y que desarrollé de la siguiente forma
realizando después una consulta en Stack Overflow.
https://es.stackoverflow.com/questions/157511/python-3-4-c%c3%b3digo-que-busca-en-una-secuencia-de-enteros-aquellos-que-son-el-res
'''

def gen_raices(min, max):
	lista = []

	# Comprueba entre tres opciones:
	# op1 = El entero no está en lista.
	# op2 = Está en lista pero de suma distintas.
	# op3 = Está en lista pero con misma suma.
	def comprueba (r1, r2):
		for d in range(len(lista)):
			if lista[d][0] == r1 + r2:
				for t in range(1,len(lista[d])):
					if r1 in lista[d][t]:
						return 3
				return (2, d)
		return 1

	# Añade a la lista las sumas de raices.
	e1 = 1
	while e1 ** 2 <= max:
		for e2 in range(1, max):
			r1 = e1 ** 2
			r2 = e2 ** 2
			if r1 + r2 <= max and r1 + r2 >= min:
				comp = comprueba(r1, r2)
				if comp == 1:
					lista.append([r1 + r2, (r1, r2)])
				elif comp == 3:
					continue
				else:
					lista[comp[1]].append((r1, r2))
		e1 += 1
	lista.sort()
	return lista

print (gen_raices(1,100))


'''
Tras la respuesta sobre una posible optimización en Stack Overflow,
el resultado fueron las siguientes mejoras.: 
'''


# PRIMERA MEJORA. DICCIONARIOS
# Con los diccionarios se elimina la función Comprobar.
# Es más eficiente buscar en un diccionario que iterar sobre una lista.
def gen_raices1(min, max):
    diccionario = {}

    # Añade a la lista las sumas de raices.
    e1 = 1
    while e1 ** 2 <= max:
        for e2 in range(1, max):
            r1 = e1 ** 2
            r2 = e2 ** 2
            if r1+r2 > max:
              continue
            if r1+r2 not in diccionario:
              diccionario[r1+r2] = []
            if (r2,r1) not in diccionario[r1+r2]:  # Esto para evitar duplicidades (1,16),(16,1) en lista asociada.
              diccionario[r1+r2].append((r1,r2))
        e1 += 1
    return diccionario


# SEGUNDA OPCIÓN. DICCIONARIOS y CONJUNTOS
# Los conjuntos solo admiten un dato si este no está ya en el conjunto.
# Para evitar duplicidades (1,16)(16,1) se ordenan antes de conjuntar.
def gen_raices2(min, max):
    diccionario = {}

    # Añade a la lista las sumas de raices.
    e1 = 1
    while e1 ** 2 <= max:
        for e2 in range(1, max):
            r1 = e1 ** 2
            r2 = e2 ** 2
            if r1+r2 > max:
              continue
            if r1+r2 not in diccionario:
              diccionario[r1+r2] = set()
            diccionario[r1+r2].add(tuple(sorted((r1,r2))))
        e1 += 1
    return diccionario


# TERCERA MEJORA. DEFAULTDICT y CONJUNTOS
# Defaultdict es tipo de diccionario que añade elemento si no está cuando se le hace una consulta.
from collections import defaultdict

def gen_raices3(min, max):
    diccionario = defaultdict(set)

    # Añade a la lista las sumas de raices.
    e1 = 1
    while e1 ** 2 <= max:
        for e2 in range(1, max):
            r1 = e1 ** 2
            r2 = e2 ** 2
            if r1+r2 > max:
              continue
            diccionario[r1+r2].add(tuple(sorted((r1,r2))))
        e1 += 1
    return diccionario


# CUARTA MEJORA. ELIMINAR ITERACIONES INNECESARIAS
# Se evita procesar rangos innecesarios ajustando los valores de r1 y r2.
# elevar a 0,5 es equivalente a hacer raiz cuadrada.
# iterar r2 empezando por r1 evita valores duplicados tipo (1,16)(16,1)
def gen_raices3(min, max):
    diccionario = defaultdict(list)
    for e1 in range(1, int(max**0.5)):
        for e2 in range(e1, int((max-e1**2)**0.5)+1):
            r1 = e1**2
            r2 = e2 ** 2
            diccionario[r1+r2].append((r1, r2))
    return diccionario


# QUINTA MEJORA. LIGERA OPTIMIZACION
# Sacar r1 ** 2 del segundo bloque.
from collections import defaultdict

def gen_raices4(min, max):
    diccionario = defaultdict(list)
    for e1 in range(1, int(max**0.5)):
        r1 = e1**2
        for e2 in range(e1, int((max-e1**2)**0.5)+1):
            r2 = e2 ** 2
            diccionario[r1+r2].append((r1, r2))
    return diccionario


'''
Como curiosidad, he cronometrado cuánto tarda en ejecutarse cada una de estas versiones, 
usando timeit (que ejecuta la función 1000 veces y se queda con el promedio 
de las tres mejores, para eliminar "ruido" aleatorio). Esto es lo que he obtenido:

    Tu versión: 745 µs
    Versión 1 (diccionarios de listas): 610 µs
    Versión 2 (diccionarios de conjuntos): 641 µs
    Versión 3 (reducir iteraciones): 44.7 µs
    Versión 4 (optimización final): 36.7 µs

'''