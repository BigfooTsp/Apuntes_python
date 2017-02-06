## PRACTICANDO MANEJO DE ERRORES ##

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



