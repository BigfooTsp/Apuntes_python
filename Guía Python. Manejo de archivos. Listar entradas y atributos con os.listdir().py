'''
Script que utiliza la librería 'os' y 'time' para leer los archivos del directorio del script
obteniendo de cada archivo su tamnañpo, fecha, útlimo acceso y última modificación.
Al final, el número total de archivos y el tamaño total.

http://python-para-impacientes.blogspot.com.es/2015/09/explorando-directorios-con-listdir-walk.html '''

# ejemplo :
	import os

	ruta_app = os.getcwd()
	listdir = os.listdir()

	print (ruta_app)
	for elemento in listdir:
	    print ("elemento: " + elemento)
	'''
	D:\Mis Documentos\Dropbox\Proyectos Phyton\Apuntes
	elemento: Basic. creación de módulos.py
	elemento: Basic. Docstrings. Creando documentación en el código.py
	elemento: Basic. eval() exec() compile().py
	elemento: Basic. Funcional I. map() filter() reduce() y lambda().py
	elemento: Basic. Funcional II. comprensión del istas, generadores y decoradores.py
	elemento: Basic. Funciones.py
	'''

# Script

	import os
	from datetime import datetime

	ruta_app = os.getcwd() # obtiene ruta del script
	contenido = os.listdir(ruta_app)
	# os.listdir(path='.') donde el argumento puede ser del tipo str o bytes
	total = 0
	archivos = 0
	formato = '%d-%m-%y %H:%M:%S' # Establece formato de fecha y hora
	linea = '-' * 40

	for elemento in contenido:
		archivo = ruta_app + os.sep + elemento # os.sep (separador utilizado en una ruta)
		if not os.access(archivo, os.X_OK) and os.path.isfile(archivo):
			# con os.X_OK verififica que no es ejecutable
			# os.path.isfile para ver si es un archivo.
			archivos +=1
			estado = os.stat(archivo) # obtiene estado del archivo
			tamaño = estado.st_size # obtiene de estado el tamaño

			# Obtiene del estado fechas del último acceso/modificiación
			# Como los valores de las fechas-horas vienen expresados en segundos
			# se convierten a tipo datetime.

			ult_acceso = datetime.fromtimestamp(estado.st_atime)
			modificado = datetime.fromtimestamp(estado.st_mtime)

			ult_acceso = ult_acceso.strftime(formato)
			modificado = modificado.strftime(formato)

			# Se acumulan los tamaños y se muestra info de cada archivo

			total += tamaño
			print(linea)
			print("archivo       :", elemento)
			print("modificado    :", modificado)
			print("ultimo acceso :", ult_acceso)
			print("tamaño (Kb    :", round(tamaño/1024, 1))

	print (linea)
	print("Núm. archivos:", archivos)
	print("total (Kb)   :", round(total/1024, 1))

''' Explicaciones:
	Modos con os.acces:
		os.X_OK  - para ver si es ejecutable.
		os.F_OK  - para comprobar que es posible acceder al archivo.
		os.R_OK  - para ver si se puede leer.
		os.W_OK  - para ver si además permite la escritura. 

	os.path.isfile(archivo) - comprueba si es un archivo


	os.stat- obtiene estado del archivo

	    st_size: tamaño en bytes.
	    st_mode: tipo de archivo y bits de permisos.
	    st_ino: número de inodo.
	    st_dev: identificador del dispositivo.
	    st_uid: identificador del usuario propietario.
	    st_gid: identificador del grupo propietario.
	    st_atime: fecha-hora del último acceso (en segundos).
	    st_mtime: fecha-hora de la última modificación (en segundos).
	    st_ctime: fecha-hora ultimo cambio (unix) o creación (win).
	    st_atime_ns, st_mtime_ns y st_ctime_ns (idem. expresado en nanoseg).
	    st_blocks: número de bloques de 512 bytes asignados.
	    st_blksize: tamaño de bloque preferido por sistema.
	    st_rdev: tipo de dispositivo si un dispositivo inode.
	    st_flags: banderas definidas por usuario.
	    st_gen: Número fichero generado.
	    st_birthtime: tiempo de creación del archivo.
	    st_rsize: tamaño real del archivo.
	    st_creator: creador del archivo.
	    st_type: tipo de archivo.
	    st_file_attributes: atributos.

	Aunque hay funciones específicas sin usar os.stat para algunas funciones.

		os.path.getsize() - obtiene tamaño del archivo
		os.path.getatime()- último acceso
		os.path.getmtime()- última modificación

'''


