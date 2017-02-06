

# VARIABLES EN PYTHON:
''' Tipos de variables:
	Variables locales: son las que 'viven' dentro de las funciones o clases.
	Variables globales: Accesibles por todo el módulo.
	Variables de clase: Las que se definen en una clase y no cambian.
	Variables de instancia: Son las que se definen en el constructor __init__ de la clase
							y se definen como parámetros.
	Diccionario  o espacio incorporado: Común en todos los módulos.

	Con el mismo nombre, siempre se accederá antes a la variable local; pero si no encuentra la
	variable en local ni global, accederá al "diccionario incorporado" común en todos los módulos.
	Si tampoco lo encuentra aquí, dará un NameError'''

# Función global
'''  : Declara una variable para que pueda ser utilizada fuera de su ámbito.'''

	km = 10  # se asigna 10 a la variable global km (fuera de la función)
	def acelerar():  # se define la función acelerar
	 global km  # ahora km podrá usarse dentro de la función
	 km+= 5  # se incrementa la velocidad en 5 km
	 
	acelerar()  # llama a la función acelerar()
	print('Velocidad:', km)  # velocidad: 15

# funciones locals() y globals()
''' devuelven diccionario con las variables locales o globales'''
	
	# http://python-para-impacientes.blogspot.com.es/2015/03/diccionarios-de-variables-locales-y.html

	from math import pi
	global1 = 1
	 
	def funcion1(x, y):
	    global global1 #import variable global
	    total = x + y + global1
	    global1 = 2 # modifica variable global
	    print("funcion1. Dicc. locales.:", locals())
	    print("funcion1. Dicc. globales:", globals())
	    return total 
	    ''' # 
	    funcion1. Dicc. locales.: {
	    'y': 10, 'total': 16, 'x': 5}

		funcion1. Dicc. globales: {
		'__name__': '__main__',
		'__file__': 'localsglobals.py',
		'global1': 2,
		'pi': 3.141592653589793,
		'__builtins__': <module 'builtins' (built-in)>,
		'__package__': None,
		'funcion1': <function funcion1 at 0xb70578e4>,
		'__cached__': None,
		'__doc__': None,
		'__loader__': <_frozen_importlib.SourceFileLoader object at 0xb70b160c>,
		'main': <function main at 0xb7057854>,
		'clase1': <class '__main__.clase1'>,
		'__spec__': None}
		 '''

	 
	class clase1:
	    z = 3
	    print("clase1. Dicc. locales.:", locals())
	    print("clase1. Dicc. Globales:", globals())
	    def __init__(self):
	        print("clase1: método __init__")
	   
	    def __call__(self):
	        print("clase1: método __call__")
	    ''' #
	    clase1. Dicc. locales.: {
	    '__qualname__': 'clase1', '__module__': '__main__', 'z': 3}

		clase1. Dicc. Globales: {
		'__name__': '__main__',
		'__loader__': <_frozen_importlib.SourceFileLoader object at 0xb70b160c>,
		'global1': 1, '__cached__': None, 'pi': 3.141592653589793,
		'__builtins__': <module 'builtins' (built-in)>,
		'__package__': None,
		'__file__': 'localsglobals.py',
		'funcion1': <function funcion1 at 0xb70578e4>,
		'__spec__': None, '__doc__': None}'''
	   
	def main():
	    a = 5
	    b = 10
	   
	    if "funcion1" in globals():
	        if callable(globals()["funcion1"]): 
	        # 'Llamada de retorno' Callable verifica si el objeto puede ser llamado, para funciones dinámicas.
	            print("Rtdo funcion1: ", globals()["funcion1"](a, b))
	  
	    objeto = clase1()
	    if "objeto" in locals():
	        if callable(locals()["objeto"]):
	            locals()["objeto"]
	 
	    locals()["a"] = 20 # No se puede modificar.
	    globals()["b"] = 20 # modifica pero accede a b.local cuando se llama
	    print("main(). Dicc. locales.:", locals())
	    print("main(). Dicc. globales:", globals()) 
	    print("a: ", a, "b:", b) 
	    return 0
		'''#
		main(). Dicc. locales.: {
		'objeto': <__main__.clase1 object at 0xb7113f4c>, 'a': 5, 'b': 10}

		main(). Dicc. globales: {
		'__name__': '__main__',
		'clase1': <class '__main__.clase1'>,
		'funcion1': <function funcion1 at 0xb70fe974>,
		'__spec__': None, '__file__': 'localsglobals.py',
		'__package__': None, '__builtins__': <module 'builtins' (built-in)>,
		'__loader__': <_frozen_importlib.SourceFileLoader object at 0xb715860c>,
		'__cached__': None, 'pi': 3.141592653589793,
		'global1': 2,
		'__doc__': None,
		'b': 20, '''

	'main': <function main at 0xb70fe89c>}	if __name__ == '__main__':
	    main()
