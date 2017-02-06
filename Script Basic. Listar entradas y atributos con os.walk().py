'''
Script que utiliza la librería 'os' y 'time' para leer los archivos del directorio del script
obteniendo de cada archivo su tamaño, fecha, útlimo acceso y última modificación.
Al final, el número total de archivos y el tamaño total.

http://python-para-impacientes.blogspot.com.es/2015/09/explorando-directorios-con-listdir-walk.html'''


# os.walk(top, topdown=True, onerror=None, followlinks=False)
'''
topdown=True - indica que la lectura se hace desde el directorio con menor profundidad.
onerror=None - ignora los errores de os.listdir (utilizada por walk desde python 3.4 
			   en lugar de os.stat en versiones anteriores).
followlinks=False ignora los enlaces simbólicos.

Cada lectura de walk devuelve una tupla con el siguiente contenido: No es una tupla en sí, si no un generador.
    root: directorio leído
    dirs: lista de directorios existentes en el directorio leído
    files: lista de archivos existentes en el directorio leído '''

# ejemplo walk:
	'''
	import os

	ruta_app = os.getcwd()
	walk = os.walk(ruta_app, topdown=True)

	print (ruta_app)
	for a, b, c in walk:
		print ("\na: ",str(a) +"\nb: ",str(b) + "\nc: ",str(c) + "\n\n")
		
		# resultado
		a:  D:\Mis Documentos\Dropbox\Proyectos Phyton\Apuntes
		b:  []
		c:  ['Basic. creación de módulos.py', 'Basic. Docstrings. Creando documentación en el código.py',
		 'Basic. eval() exec() compile().py', 'Basic. Funcional I. map() filter() reduce() y lambda().py',
		 Basic. Funcional II. comprensión del istas, generadores y decoradores.py',]
		'''

# script:

	import os
	from datetime import datetime
	 
	ruta_app = os.getcwd()
	total = 0
	num_archivos = 0
	formato = '%d-%m-%y %H:%M:%S'
	linea = '-' * 60
	 
	for ruta, directorios, archivos in os.walk(ruta_app, topdown=True):
	    print('\nruta       :', ruta) 
	    for elemento in archivos:
	        num_archivos += 1
	        archivo = ruta + os.sep + elemento
	        estado = os.stat(archivo)
	        tamaño = estado.st_size
	        ult_acceso = datetime.fromtimestamp(estado.st_atime)
	        modificado = datetime.fromtimestamp(estado.st_mtime)
	        ult_acceso = ult_acceso.strftime(formato)
	        modificado = modificado.strftime(formato)
	        total += tamaño
	        print(linea)
	        print('archivo      :', elemento)
	        print('modificado   :', modificado)        
	        print('último acceso:', ult_acceso)
	        print('tamaño (Kb)  :', round(tamaño/1024, 1))
	 
	print(linea)
	print('Núm. archivos:', num_archivos)
	print('Total (kb)   :', round(total/1024, 1))