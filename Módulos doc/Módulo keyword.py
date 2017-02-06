''' MÓDULO KEYWORD. permite obtener las palabras reservadas del lenguaje.
	Útil para diferencias entre diferentes versiones de pyyhon. '''

from keyword import iskeyword, kwlist

kwlist   # List parabras reservadas
	''' devuelve 
	['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue',
	'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
	'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
	'return', 'try', 'while', 'with', 'yield'] '''

iskeyword("exec")   # Retorna True si el término es palabra reservada
	#False
	#