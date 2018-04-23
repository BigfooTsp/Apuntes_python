''' FUNCIONES:

Las funciones deben de ser como cajas negras una vez creadas, solo debemos acordarnos de su nombre para usarlas.
Su ventaja es la de poder ser reutilizadas y por eso deben dar soluciones muy concretas. '''

# Función con parámetros obligatorios:
	def area_triangulo(base, altura):  # define función con dos parámetros
	 ''' Calcular el área de un triangulo'''  # cadena de documentación
	 return base * altura / 2  # devuelve el resultado de la expresión
	 
	print(area_triangulo(6, 4))  # la función retornará el valor 12
	print(area_triangulo(3.5, 2.4))  # la función retornará el valor 4.2

# función con parámetros opcionales:
	def distancia(*tramos):  # define función con nº variable de parámetros
	 ''' Suma distancia de tramos '''  # cadena de documentación
	 total = 0  # inicializa variable numérica 
	 for distancia in tramos:  # recorre, uno a uno, todos los tramos...
	  total = total + distancia  # … y acumula la distancia
	 return total  # devuelve la suma de todos los parámetros
	 
	tramo1 = 10
	print(distancia(tramo1, 20, 30, 40))  # la función retornará el valor 100 
	print(distancia())  # la función retornará el valor 0

# Función con valores por defecto:
	'''Se utiliza por si se omite este dato al invocar la función'''
	def pagar(importe, dto_aplicado = 5):
	 ''' La función aplica descuentos '''
	 return importe - (importe * dto_aplicado / 100)
	 
	print(pagar(1000))  # 950
	print(pagar(1000, 10))  # 900

# Función con diccionario como parámetro:
	def porc_aprobados(aprobados, **aulas):
	 ''' Calcula el % de aprobados '''
	  
	 total=0
	 for alumnos in aulas.values():
	  total += alumnos
	  
	 return aprobados * 100 / total
	 
	porcentaje_aprobados = porc_aprobados(48, A = 22, B = 25, C = 21)
	print(porcentaje_aprobados)

# Funciones sin return:
	''' como cualquier otra, pero devuelve None si es asignada a una variable o llamada desde un print. '''
	def repite(caracter='-', repite=3):
	 print(caracter * repite)
	 
	repite('=', 20)

# funciones lambda:
	''' crea funciones en una sola linea '''
	cuadrado = lambda x: x*x
	n = cuadrado(2)

# funciones dentro de funciones:
	''' me llama la atención como se llama a las funciones internas con sis '''
	def conversor(sis):
	    def sis_bin(numero):
	        print('dec:', numero, 'bin:', bin(numero))
	  
	    def sis_oct(numero):
	        print('dec:', numero, 'oct:', oct(numero))
	    
	    def sis_hex(numero):
	        print('dec:', numero, 'hex:', hex(numero))
	   
	    sis_func = {'bin': sis_bin, 'oct': sis_oct, 'hex': sis_hex}
	    return sis_func[sis]
	 
	conversorhex = conversor('hex')  # crea una instancia del conversor hexadecimal
	conversorhex(100)  # convierte el número 100 dec a hex
	print()
	conversor('bin')(9)  # otra forma de usar el conversor. Convierte 9 dec a binario


