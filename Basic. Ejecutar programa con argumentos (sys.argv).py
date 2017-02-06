''' Variable sys.argv
Donde el sistema guarda los argumentos'''

# argumentos.py
import sys
print (" Argumentos en sys.argv", sys.argv)

'''
>>> python argumentos.py
--> ['argumentos.py']

>>> python argumentos.py hola mundo
--> ['argumentos.py, hola, mundo']

# La consola devuelve una lista con los argumentos.