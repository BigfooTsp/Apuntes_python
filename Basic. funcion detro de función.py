def funcionA(x):
	def funcionB(y):
		return x+y
	return funcionB

funcion = funcionA(5)
print (funcion(3))

print (funcionA(5)(3))

print (funcion)