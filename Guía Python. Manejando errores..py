## PRACTICANDO MANEJO DE ERRORES ##
https://docs.python.org/3.4/library/exceptions.html

print("bienvenido")

n=1
d=5

try:
	print (l/5)
except TypeError:
	print("Error en tipo de datos")
except NameError:
	print("variable no existe")
except ZeroDivisionError:
	print("No se puede dividir por 0")
else:
	print("No hubo error")
finally:
	print ("Me ejecuto pase lo que pase")

print ("Seguimos...")

# Creando nuestro propio error:

class UnoError(Exception):
	def __init__(self, valor):
		self.valorError = valor
	def __str__(self):
		print("No se puede dividir entre 1 el número: ", self.valorError)

print ("\nTras crear nuestro error:\n")

try:
	if n==1:
		raise UnoError(d)
except UnoError:
	print("Se ha producido un error que yo cree")

print("\n## Uso del parámetro __str__")

if n==1:
	raise UnoError(d) #Aquí lo ejecuta segun __str__

print ("Adios")


# Objeto Exception:
try:
	print (dedfef)
except Exception as e:

	print (str(e))
	print (dir(e))

	##
	name 'dedfef' is not defined
	['__cause__', '__class__', '__context__', '__delattr__', 
	'__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
	'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
	'__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
	'__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', 
	'__subclasshook__', '__suppress_context__', '__traceback__', 'args', 
'with_traceback']

