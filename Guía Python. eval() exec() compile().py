''' EVALUAR, EJECUTAR Y COMPILAR CADENAS
	http://python-para-impacientes.blogspot.com.es/2015/03/evaluar-ejecutar-y-compilar-cadenas.html '''

# 'eval()' evalúa un string por el tipo de objeto que mejor se adapta a él, si no lo consigue, lanza error.
	precio = 5
	cadenas = ['(4+5)**2',
	           '(1, 2, 3)',
	           '["I", "II", "III"]',
	           '{"a":1, "b":2, "c":3}',
	           'len("Python")',
	           '20 * precio',
	           '__import__("platform").python_version()']
	 
	for cadena in cadenas:
	    print(cadena, "=>", eval(cadena), "Tipo:",type(eval(cadena)))
	'''
	(4+5)**2 => 81 Tipo: <class 'int'>
	(1, 2, 3) => (1, 2, 3) Tipo: <class 'tuple'>
	["I", "II", "III"] => ['I', 'II', 'III'] Tipo: <class 'list'>
	{"a":1, "b":2, "c":3} => {'c': 3, 'a': 1, 'b': 2} Tipo: <class 'dict'>
	len("Python") => 6 Tipo: <class 'int'>
	20 * precio => 100 Tipo: <class 'int'>
	__import__("platform").python_version() => 3.4.0 Tipo: <class 'str'> '''

# 'exec()' ejecuta el código de una cadena o archivo. Error si no puede.
	# Nota: En python2 exec() forma parte de las palabras reservadas del sistema, en python3 es solo una función.
	exec('secreto = input("Introducir clave secreta: ")')
	exec('if secreto == "1234": print("¡Eureka!")')
	exec('print("Clave secreta:", secreto)')

# 'compile()' compila un texto en un objeto para después utilizarlo con eval() o exec().
	''' No se utiliza mucho porque puede producir un problema de seguridad. Puede utilizarse
		para introducir código durante la ejecución de un programa.'''

	# compile() y eval():
		>>> codobjeto = compile('[1, 2, 3, 4, 5]', 'lista', 'eval')
		>>> eval(codobjeto)
		[1, 2, 3, 4, 5]

		>>> print(codobjeto)
		<code object <module> at 0xb5d8b340, file "lista", line 1>

		>>> type(codobjeto)
		code

	# compile() y exec():
		>>> codobjeto = compile('for t in range(11):print(t, t**2)', 'modcuadrado', 'exec')
		>>> exec(codobjeto)
		0 0
		1 1
		2 4
		3 9
		4 16
		5 25
		6 36
		7 49
		8 64
		9 81
		10 100

		>>> print(codobjeto)
		<code object <module> at 0xb6865a20, file "modcuadrado", line 1>

		>>> type(codobjeto)
		code
