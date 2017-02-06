import inspect:
# INTROSPECCIÓN EN PYTHON:

# https://zbutton.wordpress.com/2010/03/20/introspeccion-en-python/
# Obtener el nombre de la función donde nos encontramos y desde dónde ha sido llamada.
# ? http://www.eferro.net/2012/11/introspeccion-en-python-mediante-inspect.html

# dir: Devuleve lista de todos los elementos de un objeto
	lista = ['pedro', 2,]

	# dir sobre un objeto lista:
	print (dir (lista))
		''' ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', 
		'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
		'__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', 
		'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
		'__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', 
		'__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
		'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 
		'reverse', 'sort'] '''

	# sobre el elemento de una lista:
	print (dir (lista[0]))
		''' ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', 
		'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', 
		'__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', 
		'__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', 
		'__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 
		'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 
		'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 
		'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 
		'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 
		'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 
		'title', 'translate', 'upper', 'zfill'] '''


# getattr: Con getattr obtenemos un elemento de un objeto o módulo.
	# ... Continuando con el ejemplo anterior.
	print (getattr(lista,'__len__'))
	''' <method-wrapper '__len__' of list object at 0x003FA238>'''


# callable: Indica si el objeto (por ejemplo, la funciòn de un módulo obtenida mediante getattr, es 'llamable')


# Módulo Inspect:

	# inspect.stack()
	'''
	devuelve una lista de tuplas, cada una como 
	(frame object, 
		[0] dirección de módulo, 
		[1] línea de código en módulo, 
		[2] método, 
		[3] línea que llama, 
		[4] 0?)
	de llamada más próximo a más lejano, siendo [0] el propio que ejecuta inspect.stack
	'''

	# Ejemplo 1: Averiguar la clase y métodos.
		 
		""" Devuelve una lista de registros de las llamadas. 
		La primera entrada en la lista devuelta representa el llamador; 
		La última entrada representa la llamada más externa en la pila.
		"""
		 
		def miNombre():
			return inspect.stack()[1][3]
		 
		def deDonde():
			result=""
			for i in range(2,len(inspect.stack())-1):
				if result:
					result+="|"
				result+=inspect.stack()[i][3]
			return result
		 
		def primera():
			print("Estoy en la función '%s', ha sido llamada desde: %s" % (miNombre(), deDonde()))
			segunda()
		 
		def segunda():
			print("Estoy en la función '%s', ha sido llamada desde: %s" % (miNombre(), deDonde()))
			tercera()
		 
		def tercera():
			print("Estoy en la función '%s', ha sido llamada desde: %s" % (miNombre(), deDonde()))
			 
		primera()
		segunda()

	# Ejemplo 2: Obtener clases y funciones de un módulo concreto
		import sys
		import inspect
		import os.path
		import os


		def get_symbols_from_module(python_module, filter_func):
		    members = inspect.getmembers(python_module)
		    return dict([[name,symbol] for name,symbol in members 
		                               if filter_func(symbol)])

		def main():
		    # Obtain a map whith all the classes defined in the 
		    # standard os module
		    print (get_symbols_from_module(os, inspect.isclass))
		    print()

		    # Obtain a map with all the functions defined in the
		    # standard sys module
		    print (get_symbols_from_module(sys, inspect.isfunction))

		if __name__ == '__main__':
		   main()

		'''devuelve:
		{'MutableMapping': <class 'collections.abc.MutableMapping'>, 
		'error': <class 'OSError'>, 'stat_result': <class 'os.stat_result'>, 
		'_wrap_close': <class 'os._wrap_close'>, 'terminal_size': <class 'os.terminal_size'>, 
		'_Environ': <class 'os._Environ'>, 'times_result': <class 'nt.times_result'>, 
		'uname_result': <class 'nt.uname_result'>, 'statvfs_result': <class 'os.statvfs_result'>}

		{'__interactivehook__': <function enablerlcompleter.<locals>.register_readline at 0x017D2270>} '''
