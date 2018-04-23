Filtrando archivos con los módulos glob y fnmatch.
'''
 El primero busca en directorios. El segundo itera sobre una lista buscando coincidencias con un patrón.

	http://python-para-impacientes.blogspot.com.es/2015/09/filtrando-archivos-y-directorios-con.html '''

# MÓDULO GLOB. Busqueda directamente en directorios coincidencias con un patrón.
	glob.glob(pathname, recursive=False) # Devuleve listado con resultado de patrón "pathname".
		# puede ser recursiva (busca dentro de resultados, por ej, en archivos) y las rutas absolutas o relativas.
		# Permite comodines tipo comandos unix (no expresiones regulares).
			? Un carácter:	
			* Uno o más caracteres:	'../../../img/201?/*'	
			[] Caracteres permitidos: '/home/ant/img/201[45]'	
			[!] Caracteres no permitidos: '/home/ant/img/201[!45]'	
			[-] Rango caracteres permitidos	'/home/ant/img/201[0-9]'
			(A partir de Python 3.5) ** Búsqueda recursiva,	con recursive=True (se incluyen archivos). 
				'/home/ant/img/2015/**' : ('/home/ant/img/2015/Granada/1.jpg','/home/ant/img/2015/Granada/2.jpg')
				'/home/ant/img/2015/**/*.jpg' : ('/home/ant/img/2015/Granada/1.jpg', '/home/ant/img/2015/Granada/2.jpg')

		# ejemplo:
			import glob
			raices = ['/home/ant/img/201?', # '/home/ant/img/2013', '/home/ant/img/2014'
			          '../../img/201?/*', # '/home/ant/img/2014/Huelva''/h, ome/ant/img/2014/Sevilla'
			          '/home/ant/img/201[345]', # '/home/ant/img/2014', '/home/ant/img/2015' 
			          '/home/ant/img/201[!345]', # 	'/home/ant/img/2012
			          '/home/ant/img/201[0-9a-z]', # '/home/ant/img/2013'
			          '../../img/2015/F*/*.JPG'] # '/home/ant/img/2015/Final/campeón.jpg'
			 
			for raiz in raices:
			    print('\n'+raiz)
			    rutas = glob.glob(raiz)
			    print('rutas:', len(rutas))
			    for ruta in rutas:
			        print(ruta)
			 
			# glob con un patrón que utiliza recursividad, Se obtienen los directorios y archivos coincidentes
			 
			raiz = '/home/ant/img/2015/**'
			rutas = glob.glob(raiz, recursive=True)
			print('\nrutas:', len(rutas))
			for ruta in rutas:
			    print(ruta)

	glob.iglob (pathname, recursive=False) # devuelve iterador en lugar de lista lo que permite procesarlo directamente sin asignarlo antes.
		raiz = '/home/ant/img/2015/**'
		for ruta in glob.iglob(raiz, recursive=True):
		    print(ruta)

	glob.escape(pathname) # (desde python 3.4) Permite en pathname carácteres especiales, coincidentes con los comodines.
		# glob.escape('/Viajar?.txt') equivale a glob.glob(/Viajar[?].txt)


# MÓDULO FNMATCH. busca coincidencias de un archivo con un patrón.

	# fnmatch.fnmatch(archivo, patrón) > Devuelve True si coincide con patrón, diferencia mayúsculas o minúsculas si el sistema operativo lo hace. '''
		# ejemplo:
		import os, fnmatch 
		for archivo in os.listdir('.'):
		    if fnmatch.fnmatch(archivo.upper(), '*.MD'): # interpreta el archivo en mayúsculas.
		        print(archivo)

	# fnmatch.fnmatchcase(filename, pattern) > True si coincide. Diferencia mayúsculas y minúsculas en cualquier caso.

	# fnmatch.traslate('patrón')  > traduce los comodines a una expresión regular.
		expresion_regular = fnmatch.translate('*.md')
		print('Expresión regular:', expresion_regular) # .*\.md\Z(?ms)