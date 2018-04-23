# TRABAJAR CON FICHEROS:

''' Modos:
	r	Lectura
	r+	Lectura/Escritura
	w	Sobreescritura. Si no existe archivo se creará
	a	Añadir. Escribe al final del archivo
	b	Binario
	+	Permite lectura/escritura simultánea
	U	Salto de línea universal: win cr+lf, linux lf y mac cr
	rb	Lectura binaria
	wb	Sobreescritura binaria
	r+b	Lectura/Escritura binaria '''

''' 'open' abre el fichero	> open ("archivo", "modo") '''
	ObjArchivo = open('/home/archivo.txt', mode='r', encoding='utf-8') 
	# por defecto modo r y encoding sistema

'''	'close' cierra el fichero	> close ("archivo")'''
	ObjArchivo.close
	# Lo libera de la memoria.

''' Leer Archivo '''
	# 'read(número de bytes)'
		archivo = open('archivo.txt','r')  # abre archivo en modo lectura
		cadena1 = archivo.read(9)  # lee los 9 primeros bytes
		cadena2 = archivo.read()  # lee la información restaste
		print(cadena1)  # muestra la primera lectura
		print(cadena2)  # muestra la segunda lectura
		archivo.close  # cierra archivo 

	# 'readlines(bytes)'  Lee las lineas del archivo como una lista
		archivo = open('archivo.txt','r')  # abre archivo en modo lectura
		while True:  # inicia bucle infinito para...
		linea = archivo.readline()  # … leer línea a línea
		if not linea: break  # … hasta que no haya más que leer
		print(linea)  # muestra la línea leída
		archivo.close  # cierra archivo

	# with-as lee el fichero y lo cierra automáticamente al finalizar.
		with open("indice.txt") as fichero:  # abre archivo (y cierra cuando termine lectura)
		for linea in fichero:  # recorre línea a línea el archivo
		print(linea)  # muestra línea última leída

''' Escribir fichero '''
	# 'write' escribe una cadena en un fichero (Lo crea si no existe).
		cadena1 = 'Datos'  # declara cadena1
		cadena2 = 'Secretos'  # declara cadena2
		archivo = open('datos1.txt','w') # abre archivo para escribir
		archivo.write(cadena1 + '\n')  # escribe cadena1 añadiendo salto de línea
		archivo.write(cadena2) # escribe cadena2 en archivo
		archivo.close  # cierra archivo

	# 'writelines' escribe una lista a un fichero.
		lista = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']  # declara lists
		archivo = open('datos2.txt','w')  # abre archivo en modo escritura
		archivo.writelines(lista)  # escribe toda la lista en el archivo
		archivo.close  # cierra archivo

''' Mover el puntero en el archivo '''
	# 'seek(byte)' mueve el puntero y 
	# 'tell' devuelve la posición de este
	archivo = open('datos2.txt','r')  # abre archivo en modo lectura
	archivo.seek(5)  # mueve puntero al quinto byte
	cadena1 = archivo.read(5)  # lee los siguientes 5 bytes
	print(cadena1)  # muestra cadena
	print(archivo.tell())  # muestra posición del puntero
	archivo.close  # cierra archivo

''' Módulo Pickle ('dump' y 'load')
	lee y escribe cualquier objeto python con sus métodos 'dumb' y 'load'
	para escribir y leer datos.'''
	import pickle  # importa módulo pickle
	lista = ['Perl', 'Python', 'Ruby']  # declara lista
	archivo = open('lenguajes.dat', 'wb')  # abre archivo binario para escribir 
	pickle.dump(lista, archivo)  # escribe lista en archivo
	archivo.close  # cierra archivo
	del lista  # borra de memoria la lista
	 
	archivo = open('lenguajes.dat', 'rb')  # abre archivo binario para leer
	lista = pickle.load(archivo)  # carga lista desde archivo
	print(lista)  # muestra lista
	archivo.close  # cierra archivo


# Ejemplo:

	manejador = open("index.html", "a") # manejador para crear fichero.

	# creamos un archivo html
	html = "<! DOCTYPE HTML>\n"
	html += "<html>\n"
	html += "<head>\n"
	html += "<title>Hola mundo</title>\n"
	html += "</head>\n"
	html += "<body>\n"
	html += "<h1>Hola Mundo</h1>"
	html += "</body>\n"
	html += "</html>\n"

	manejador.write(html) # Escribe el fichero

	manejador.close() # cierra el fichero

	print ("\nDocumento HTML creado con éxito")

VER TAMBIÉN:
	Módulo glob y fnmatch (para filtrar ficheros).
	Módulo fileinput (para procesar varios ficheros a la vez).

