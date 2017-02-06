# MANEJAR ARCHIVOS Y DIRECTORIOS CON SHUTIL
	# http://python-para-impacientes.blogspot.com.es/2015/10/copiar-mover-y-borrar.html
	# http://python-para-impacientes.blogspot.com.es/2015/10/empaquetando-y-desempaquetando-archivos.html


# COPIAR ARCHIVOS:

	# shutil.copyfileobj(fsrc, fdst[, length]) > Copia archivo. (lenght es el tamaño del buffer)

		# Copia de un archivo completo.
			import shutil, os

			ruta = os.getcwd() + os.sep
			origen = ruta + 'origen.txt'
			destino = ruta + 'destino.txt'
			 
			if os.path.exists(origen):
			    with open(origen, 'rb') as forigen:
			        with open(destino, 'wb') as fdestino:
			            shutil.copyfileobj(forigen, fdestino)
			            print("Archivo copiado")

		# Copia de un archivo desde el byute 21
			import shutil, os
			 
			ruta = os.getcwd() + os.sep
			origen = ruta + 'origen.txt'
			destino = ruta + 'destino.txt'
			 
			if os.path.exists(origen):
			    forigen = open(origen,'rb')
			    forigen.seek(21) # coloca puntero en byte 21.
			    with open(destino, 'wb') as fdestino:
			            shutil.copyfileobj(forigen, fdestino)
			            print("Archivo copiado")

	# shutil.copyfile(src, dst, *, follow_symlinks=True) > Copia archivo sin metadatos.
		# (OS.error si destino no tiene permisos de escritura)
		# symlinks=False creará un enlace simbólico si el origen es otro enlace simbólico.

	# shutil.copymode(src, dst, *, follow_symlinks=True) > Copia los permisos de un archivo.
		# Follow_symlinks intentará modificar archivo destino (desde python 3.3)

		import shutil, os, stat
	 	# Antes:
		# -r--r--r-- 1 usuario usuario origen.txt
		# -rw-rw-r-- 1 usuario usuario destino.txt
		 
		ruta = os.getcwd() + os.sep
		origen = ruta + 'origen.txt'
		destino = ruta + 'destino.txt'
		if os.path.exists(origen) and os.path.exists(destino):
		    print('Antes  :', oct(stat.S_IMODE(os.stat(destino).st_mode)))
		    shutil.copymode(origen, destino)
		    print('Después:', oct(stat.S_IMODE(os.stat(destino).st_mode)))
		 
		# Después:
		# -r--r--r-- 1 usuario usuario origen.txt
		# -r--r--r-- 1 usuario usuario destino.txt

	# shutil.copystat(src, dst, *, follow_symlinks=True) > Copia estado de archivo (permiso, fechas-horas)

	# shutil.copy(src, dst, *, follow_symlinks=True) > Copia archivo con permisos.

	# shutil.copy2(src, dst, *, follow_symlinks=True) > Copia archivo con permisos y metadatos.

	# shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False)
		# Copia directorio con todos sus subdirectorios y archivos a un destino que no debería existir.
		# argumento ignore referencia a shutil.ignore_patterns()
		# symlinks=True copiará enlaces como enlaces. Si es = False no los copiará
		# ignore dangling_symlinks omite registro en log de errores de enlaces omitidos si symlinks=False.

	# shutil.ignore_patterns() > configura directorios que se omitiran en el copiado utilizando patrones tipo glob()
	import shutil, os
	 
	ruta = os.getcwd() + os.sep
	origen = ruta + 'dir1'
	destino = ruta + 'dir2'
	ignorar_pat = shutil.ignore_patterns('*.dat', 'destino.txt', 'dir11')
	 
	if os.path.exists(origen):
	    try:
	        # Si ignore=None no se excluyen archivos/directorios
	                 
	        arbol = shutil.copytree(origen, destino, ignore=ignorar_pat) 
	        print('Árbol copiado a', arbol)
	    except:
	        print('Error en la copia')

# BORRAR ARCHIVOS.

	# shutil.rmtree(path, ignore_errors=False, onerror=None) > Borra un arbol de directorios completo.
	# ignore_errors=True ignora los errores del borrado.
	# onerror indica con que función gestionar estos errorres.

# MOVER ARCHIVOS.

	# shutil.move(src, dst, copy_function=copy2) > Mueve archivo o directorio.

# OTRAS FUNCIONES.

	# shutil.disk_usage(path) > Obtiene informnación del espacio en disco.
		import shutil, os
		ruta = os.getcwd()
		datos = shutil.disk_usage(ruta)
		print('Espacio total (bytes): ', datos.total)
		print('Espacio usado (bytes): ', datos.used)
		print('Espacio libre (bytes): ', datos.free)

	# shutil.chown(path, user=None, group=None) > Cambia propietario y grupo de archivos o directorio. (Linux, python 3.3)

	# shutil.which(cmd, mode=os.F_OK | os.X_OK, path=None) > obtener ruta de ejecutable o None si no ahy acceso. (Python 3.3)
		# mode indica si un erchivo existe y es ejecutable.
		# path, si no se especifica, buscará ejecutable en variables de entorno.
		import shutil, os
		 
		archivo = 'python3.5'
		ruta = shutil.which(archivo)
		print(ruta) # /usr/local/bin/python3.5
		

# ARCHIVOS COMPRIMIDOS CON SHUTIL (python 3.2)

	# shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])
		# empaqueta archivo
		'''
		base_name: ruta y nombre del paquete a crear.
		format: formato del archivo: zip, tar, bztar. El formato xztar es soportado desde Python 3.5.
		root_dir: directorio a empaquetar (raíz).
		base_dir: directorio a empaquetar incluyendo path.
		dry_run: Si su valor es True no se creará el paquete, pero todas las operaciones que se ejecuten
				 se registrarán en un archivo log.
		Los valores de los argumentos owner (propietario) y group se asignarán al paquete. 
				Si se omiten, se asignarán los valores actuales del propietario y grupo.
		Logger: por lo general se corresponde con una instancia de logging.Logger que permitirá registrar 
				todas las operaciones que se realicen durante el archivado. '''
		
		# Ejemplo comprimir una carpeta:
			import shutil
			 
			archivo_zip = shutil.make_archive("viaje", "zip", "carpeta-fotos")
			print("Creado el archivo:", archivo_zip)

		# Ejemplo comprime una carpeta y subdirectorios.

			archivo_zip = shutil.make_archive("viaje", "zip", base_dir ="carpeta-fotos")

		# Ejemplo empaquetar archivos creando un .log
			import shutil, logging
			logging.basicConfig(level=logging.DEBUG,
			    format='%(asctime)s : %(levelname)s : %(message)s',
			    filename = 'viaje.log',
			    filemode = 'w',)
			logging.info("Inicio del proceso")
			archivo_zip = shutil.make_archive("viaje",
			    "zip", 
			    base_dir ="carpeta-fotos", 
			    logger=logging)
			logging.info("Fin del proceso")


			'''viaje.log:
			2015-10-30 20:44:01,147 : INFO : Inicio del proceso
			2015-10-30 20:44:15,167 : INFO : creating 'viaje.zip' and adding 'carpeta-fotos' to it
			2015-10-30 20:44:15,199 : INFO : adding 'carpeta-fotos/foto5.jpg'
			2015-10-30 20:44:15,224 : INFO : adding 'carpeta-fotos/foto4.jpg'
			2015-10-30 20:44:15,248 : INFO : adding 'carpeta-fotos/foto2.jpg'
			2015-10-30 20:44:15,272 : INFO : adding 'carpeta-fotos/foto1.jpg'
			2015-10-30 20:44:15,295 : INFO : adding 'carpeta-fotos/foto3.jpg'
			2015-10-30 20:44:29,212 : INFO : Fin del proceso'''

	# shutil.unpack_archive(filename[, extract_dir[, format]]) > Desempaquetar archivos.
		'''
		filename: nombre del archivo comprimido (puede incluir el path).
		extract_dir: nombre del directorio destino donde se descomprimirá el archivo. 
				Si no se indica, se asumirá el directorio de trabajo actual.
		format es el formato de archivo comprimido: zip, tar, gztar o cualquier otro formato 
				de descompresión registrado con la función register_unpack_archive().'''

		archivo_zip = shutil.unpack_archive('fotos-viaje.zip','fotografias')

	# shutil.get_archive_formats() > Obtiene formatos compatibles para empaquetar.

		'''Salida: 

		[('bztar', "bzip2'ed tar-file"),
		('gztar', "gzip'ed tar-file"),
		('tar', 'uncompressed tar file'),
		('zip', 'ZIP file')]'''

	# register_archive_format() > Permite registrar nuevos formatos para comprimir archivos.

	# shutil.get_unpack_formats() > Obtiene lista con formatos permitidos para desempaquetar.

	# register_unpack_format() > Permite registrar nuevos formatos para descomprimir.

	# shutil.register_archive_format(name, function[, extra_args[, description]]) > 
		# registra en el sistema nuevo formato para empaquetar

	# shutil.unregister_archive_format(name) > Suprime formato de empaquetar del sistema.

	# shutil.register_unpack_format(name, extensions, function[, extra_args[, description]])
		# registra en sistema formato para empaquetar.

	# shutil.unregister_unpack_format(name) > Suprime del sistema formato para empaquetar.




