
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
