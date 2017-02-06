'''
COLORAMA: Dar colores a las salidas en consola.
http://python-para-impacientes.blogspot.com.es/2016/09/dar-color-las-salidas-en-la-consola.html


# Parámetros:

	Estilos*	(Style)
	Débil	DIM
	Normal	NORMAL
	Brillante	BRIGHT
	Reset	RESET_ALL

	Colores Texto/Fondo	(Fore/Back)
	Negro	BLACK
	Rojo	RED
	Verde	GREEN
	Amarillo	YELLOW
	Azul	BLUE
	Morado	MAGENTA
	Cian	CYAN
	Blanco	WHITE
	Reset	RESET
	'''

# Ejemplo:

	from colorama import init, Fore, Back, Style
	 
	# Para restablecer los colores después de cada impresión inicializar 
	# el módulo con init(autoreset=True) en lugar de init().
	 
	init()
	print(Fore.RED + "Texto color rojo")
	print(Back.WHITE + "Texto color rojo sobre fondo blanco")
	print(Back.WHITE + Style.BRIGHT + "Texto color rojo brillante sobre fondo blanco" + Back.RESET)
	print(Style.RESET_ALL + "Texto con valores por defecto (Normalmente, blanco sobre negro)")
	print(Fore.WHITE + Back.BLUE + "Texto blanco sobre fondo azul" + Back.RESET)
	print("Texto blanco sobre fondo negro")
	 
	# Niveles de intensidad
	 
	print(Style.DIM + Fore.WHITE + "Intensidad baja")
	print(Style.NORMAL + "Intensidad normal")
	print(Style.BRIGHT + "Intensidad alta")

'''
Desplazar el cursor antes de dar formato:

	Colorama incluye la clase Cursor que permite, antes de dar formato, desplazar el cursor a una posición 
	absoluta de la pantalla o una posición relativa en relación a la posición actual: 

	Cursor.POS(columna, fila): desplaza el cursor a la fila y columna indicadas.
	Cursor.UP(número): desplaza el cursor a la línea anterior. 
	Cursor.DOWN(número): desplaza el cursor a la línea siguiente. 
	Cursor.FORDWAR(número): avanza el cursor un número de caracteres en la línea actual.
	Cursor.BACK(número): retrocede el cursor un número de caracteres en la línea actual.
	'''
	from time import sleep
	from colorama import Cursor, init, Fore
	# simulando copia de archivos
	init()
	print("Copiando archivos... ")
	for archivo in ["111", "222", "333", "444", "555"]:
	    sleep(1)
	    print(Cursor.UP(1) + Cursor.FORWARD(20) + Fore.YELLOW + str(archivo))
	        
	print(Cursor.POS(2,25) + Fore.GREEN + ">>> Proceso finalizado")