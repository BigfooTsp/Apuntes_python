# Creación de módulos.

''' 
Conceptos básicos:
	Lá forma más sencilla de hacerlo es mediante la creación de un archivo con extensión .py

	Un archivo complilado .pyc es más rápido y es independiente de la plataforma.

	de un módulo se puede importar solo aquellas funciones que nos interesan y así evitamos tener que meter el 
	nombre cada vez que lo utilizamos (from math import pi: print (pi)) pero puede causar conflictos con otros
	nombres de funciones iguales de otros módulos.

__name__
	Para hacer referencia a un elemento de un módulo se utiliza su namespaces seguido de un punto (mod.función)
	aunque se le puede poner un alias en el momento de su importación mediante as (import modulo as mod).
	Mediante el atributo __name__ tenemos acceso al nombre del módulo y podemos saber si este es importado o no si
	if __name__=="main":

dir()
	dir() lista los identificadores de un objeto. Para un módulo incluyen las funciones, las variables, las clases.'''

	import sys
	dir(sys)

	'''
	['__displayhook__', '__doc__', '__excepthook__', '__name__', '__package__', '__stderr__', '__stdin__', 
	'__stdout__', '_clear_type_cache', '_current_frames', '_getframe', '_mercurial', '_xoptions', 'abiflags', 
	'api_version', 'argv', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 
	'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit',
	'flags', 'float_info', 'float_repr_style', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 
	'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 
	'gettrace', 'hash_info', 'hexversion', 'int_info', 'intern', 'last_traceback', 'last_type', 
	'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 
	'platform', 'prefix', 'ps1', 'ps2', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit',
	'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'subversion', 'version', 'version_info',
	'warnoptions'] '''

# Paquetes (Packages)
'''
 Las variables van dentro de las funciones, las variables globales en los módulos, y estos organizados dentro
 de carpetas especiales llamados paquetes.
 Cada paquete debe tener un archivo __init__.py obligatoriamente, aunque esté vacío.
 NO es obligatorio que todos los módulos pertenezcan a un paquete.
 Cada paquete puede contener subpaquetes.'''

# convenciones:
'''
Los atributos de datos tienen preferencia sobre los métodos con el mismo nombre; 
para evitar conflictos de nombre accidentales, que pueden causar errores difíciles de encontrar en programas grandes, 
es prudente usar algún tipo de convención que minimice las posibilidades de dichos conflictos.
Algunas convenciones pueden ser poner los nombres de métodos con mayúsculas, 
prefijar los nombres de atributos de datos con una pequeña cadena única (a lo mejor sólo un guión bajo), 
o usar verbos para los métodos y sustantivos para los atributos.

'''