'''
PROCESAR VARIOS ARCHIVOS A LA VEZ CON FILEINPUT.

	http://python-para-impacientes.blogspot.com.es/p/indice.html.

Este módulo permite trabajar sobre varios archivos pasados como lista o argumentos de función.
Permite trabajar también con archivos comprimidos

# Ejemplos:

	Archivos:
		cine1.txt 
			Título;Dirección;País
			El clan;Pablo Trapero;Argentina
			Papeles en el Viento;Juan Taratuto;Argentina
			El club;Pablo Larraín;Chile
			El botón de nácar;Patricio Guzmán;Chile
		cine2.txt 
			Título;Dirección;País
			Gente de bien;Franco Lolli;Colombia
			Los hongos;Oscar Ruiz Navia;Colombia
			Manos sucias;Josef Kubota Wladyka;Colombia
			Amama;Asier Altuna;España
			Un día perfecto;Fernando León de Aranoa;España
			El desconocido;Dani de la Torre;España
		cine3.txt 
			Título;Dirección;País
			600 millas;Gabriel Ripstein;México
			Archivo 253;Abe Rosenberg;México
			El cumple de la abuela;Javier Colinas;México
			Lo que lleva el río;Mario Crespo;Venezuela

# fileinput.input(files=None, inplace=False, backup='', mode='r', openhook=None)  
	Recorre los archivos y muestra sus líneas en salida estandar (pantalla).
	El argumento Openhook permite controlar la forma de abrir archivos.


# fileinput.lineno()	
	Obtiene el número de línea. '''

	import fileinput
	import sys, glob
	 
	cines = ["cine1.txt", "cine2.txt", "cine3.txt"]
	for linea in fileinput.input(cines):
	    ln = str(fileinput.lineno())     
	    sys.stdout.write(ln + " -> " + linea)
	 
		'''
		Salida:
		1 -> Título;Dirección;País
		2 -> El clan;Pablo Trapero;Argentina
		3 -> Papeles en el Viento;Juan Taratuto;Argentina
		4 -> El club;Pablo Larraín;Chile
		... '''

# fileinput.isfirstline()   Resuelve si es la primera línea. ej:
	 if not fileinput.isfirstline():

# Recorriendo archivos con with - as
	with fileinput.input(["cine1.txt", "cine2.txt"]) as archivo:
	    for linea in archivo:
	        if not fileinput.isfirstline():
	            sys.stdout.write(linea)

# fileinput.filename(): Devuelve nombre del archivo que se está leyendo en un momento dado. 
	# Antes de leer la primera línea devuelve None.

# fileinput.fileno(): Devuelve número (descriptor) de archivo. 
	# Antes de leer la primera línea y con el proceso entre dos archivos devuelve -1.

# fileinput.filelineno(): Devuelve el número de línea leída del archivo actual. 
	# Antes de leer la primera línea devuelve 0 y tras la última línea devuelve su nº línea.

# fileinput.isstdin(): Devuelve True si la última línea se ha leído desde la entrada estándar 
	# (sys.stdin), de lo contrario devuelve False.

# fileinput.nextfile(): Cierra el archivo actual y salta al siguiente archivo si fuera posible. 
	#No se puede utilizar para omitir el primer archivo.

# fileinput.close(): Finaliza el proceso

# Cod. Trabajar con archivos filtrados por glob.glob():
	archivos = glob.glob("cine*.txt")
	archivos.sort()
	for linea in fileinput.input(archivos):
	    if not fileinput.isfirstline():
	        linea = linea.rstrip() # rststrip despoja del final de la cadena carácteres en blanco.
	        pais = linea.split(";")
	        if pais[2] == "Colombia":
	            print(linea)
	 
	'''
	Salida:
	Gente de bien;Franco Lolli;Colombia
	Los hongos;Oscar Ruiz Navia;Colombia
	Manos sucias;Josef Kubota Wladyka;Colombia'''

# Cod. Procesar archivos como argumentos de un script:
	'''Para ejecutar el script "peliculas.py" desde la línea de comandos: 
	$ python peliculas.py cine1.txt cine2.txt cine3.txt'''

	# peliculas.py
	import fileinput, sys
	 
	cines = sys.argv[1:]
	print("Archivos:", cines)
	for linea in fileinput.input(cines):
	    if not fileinput.isfirstline():
	        sys.stdout.write(linea)
	 
	'''
	Salida:
	Archivos: ['cine1.txt', 'cine2.txt', 'cine3.txt']
	El clan;Pablo Trapero;Argentina
 '''

# Cod. Procesar multimples líneas de la entrada estandard (stdin) (rstrip)
	''' Muestra las tres primeras líneas de texto introducidas'''
	print("Introducir varias líneas de texto (Finalizar - CTRL+D):")
	for linea in fileinput.input():
	    print(linea.rstrip())
	    if fileinput.lineno() == 3:
	        fileinput.close()

# Cod. Procesar archivos con la salida estandar (argumentos: inplace= True, backup='')
	''' inplace (in-situ) permite modificar archivos utilizando la salida estandard (stdout),
	con backup salvamos el archivo original con extensión .bck '''
	for linea in fileinput.input(["sala1.txt", "sala2.txt"], 
                             inplace=True, backup='.bck'):
    nl = str(fileinput.lineno()) 
    linea = nl + ": " + linea.rstrip('\n')
    print(linea)

# class fileinput.FileInput(files=None, inplace=False, backup='', mode='r', openhook=None)
	''' clase que permite crear objetos tipo fileinput con los mismos métodos que 
	fileinput.input() + readline() y __getitem__().
	openhook=fileinput.hook_encoded("utf-8") Abre archivos utilizando una codificación determinada.
	openhook=fileinput.hook_compressed . Para abrir archivos comprimidos. '''

	objfi=fileinput.FileInput(["cine1.txt", "cine2.txt"])
	while True:
		linea=objfi.readline() # lee las líneas de los archivos de entrada. 
		if not linea: break   
		if not objfi.isfirstline():
		    sys.stdout.write(linea)