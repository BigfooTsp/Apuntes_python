MÓDULO re (Expresiones regulares)
	# http://python-para-impacientes.blogspot.com.es/2014/02/expresiones-regulares.html

# COMODINES:
	'''
	.	Un solo carácter. Cualquiera menos \n
	\	Caracter especial (escapa el siguiente caracter)
	|	Alternativas entre diferentes expresiones (or)
	()	Grupos aislados.
	[]	Rangos de números, alfabéticos y especiales.
	\d  Cualquier carácter que sea dígito
	\D  Cualquier carácter que no sea dígito
	\w  Cualquier carácter alfanumérico
	\W  Cualquier carácter no alfanumérico
	\s  Espacio en blanco
	\S  Cualquier carácter que no sea espacio
	+  El carácter de la izquierda aparecerá una o varias veces
	*  El carácter de la izquierda aparecerá cero o más veces
	?  El carácter de la izquierda aparecerá cero o una vez
	{}  Indica el número de veces que debe aparecer el carácter de la izquierda:
		{3} 3 veces; {1,4} de 1 a 4; {,3} de 0 a 3; {2,} dos o más veces
	^ 	Principio del texto.
	$	Final del texto. '''

# MÉTODOS:

	# match(expresiónregular, cadena, [flag]) > Comprueba coincidencia de expresión regular con principio de string.
		# flag re.IGNORECASE:  No se hará diferencia entre mayúsculas y minúsculas
		# flag re.VERBOSE:  Los comentarios y espacios son ignorados (en la expresión).

	# search(patrón, cadena, [flag]) > Como match pero dichas coincidencias pueden aparecer en cualquir lugar.

	# group() > devuelve cadena encontrada si coincide o lanza exepción.
		import re
		mo = re.match('ftp://.+\com', 'ftp://ovh.com')
		print(mo.group())  # ftp://ovh.com 
		 
		# Con los paréntesis acotamos los grupos:
		 
		import re
		mo = re.match('ftp://(.+)\com', 'ftp://ovh.com')
		print(mo.group(0))  # ftp://ovh.com 
		print(mo.group(1))  # ovh. 
		print(mo.groups())  # ('ovh.',). 

	# start() y end() > Devuelve posiciones si está el patrón en la cadena.
		mo1 = re.search('agua', 'paraguas')
		print(mo1.start())  # devuelve 3
		print(mo1.end())  # devuelve 7

	# findall(patrón, cadena, [flag]) > devuelve lista con subcadenas coincidentes.

	# finditer(patrón, cadena) > devuelve tupla con posiciones de subcadenas coincidentes.
		cadena = 'tengo una yama que yama se llama'
		iterador = re.finditer('ama', cadena) # <_sre.SRE_Match object; span=(11, 14), match='ama'> ...
		for encontrado in iterador:
		    print(encontrado.span())  # muestra: (11, 14) , (20, 23) , (29, 32)

	# compile () > crea un objeto especial regex.object para utilizarlo posteriormente con sub(), subn(), split()

	# compile con sub(cadenaparasustituir, cadenadondesebusca, [count=número]) > sustituye nº de veces=count
		import re
		clave = "asdb92z$"
		patron = re.compile("\D")   # \D se refiere a cualquier carácter que no es un número 
		nueva_clave = patron.sub("0", clave)   # Se sustituyen los caracteres encontrados por "0"
		#Otra forma de expresarlo: nueva_clave = re.compile("\D").sub("0", clave)
		print(nueva_clave)   # 00009200
		 
		#Para motrar el tipo de objeto de "patron":
		orint(type(patron))
		 
	# subn() > Como sub pero devuelve una tupla con dos resultados: [0] = cadena nueva, [1] = carácteres cambiados.
	
	# compile con split(cadena, [maxsplit=0]) > devuelve cadena en subcadenas.
		import re
		meses = 'ene+feb+mar+abr+may+jun'
		 
		patron = re.compile('\+')
		print(patron.split(meses))  # ['ene', 'feb', 'mar', 'abr', 'may', 'jun']
		 
		patron = re.compile('\+')
		print(patron.split(meses, maxsplit=1))  # ['ene', 'feb+mar+abr+may+jun']	

