# DOCSTRINGS

''' Documentando código: El texto entre comillas redacta el docstring del módulo.

	En modo interactivo: 
		> help(módulo)

	En linea de comandos: 
		> $ pydoc3 módulo
		> $ pydoc3 -w módulo # guarda el docstring en html
		> $ pydoc3 -k geometri # Busca en docstring
		> $ pydoc3 -p 8080 # inicia servidor web (puerto 8080) con la docstring (en http://localhost:8080)

	Dentro del módulo:
	'''
		def area_trapecio(BaseMayor, BaseMenor, Altura):
		 '''area_trapecio: Calcula el área de un trapecio.
		 area_trapecio = (BaseMayor + BaseMenor) * Altura / 2'''
		 return (BaseMayor + BaseMenor) * Altura / 2
		   
		print(area_trapecio(10,4,4))  # Resultado: 28

		print(area_trapecio.__doc__)  # area_trapecio: Calcula el área de un trapecio.
 								  # area_trapecio=(BaseMayor+BaseMenor)*Altura/2

