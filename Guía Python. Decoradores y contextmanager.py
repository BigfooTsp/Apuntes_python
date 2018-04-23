'''
Los decoradores son funciones que reciben como argumento otra función y devuelven la 
función modificada.

Un generador de contexto permite ejecutar una función dentro de un contexto.

ejemplo manejando errores:
	Un posible uso sería el de generar un bloque try-except sobre el que volcar varias funciones
	que requieran de este control en lugar de escribirlo en todas las funciones por separado.'''

	def main():
	    func_error()


	def decorador(func):
	    def mierror(**kwargs):
	        try:
	            func(**kwargs)
	        except Exception as er:
	            print ("Ha habido un error de tipo %s" %er)
	    return mierror


	@decorador
	def func_ok():
	    print ("Funcionamiento correcto")


	@decorador
	def func_error():
	    raise KeyError("función fallando")

#Ejemplo 1 (con contextmanager)
	import contextlib

	@contextmanager
	def tag(name):
	    print("<%s>" % name)
	    yield # representa la función
	    print("</%s>" % name)

	'''    
	with tag('H1'):
		print('Title')

	Genera:
	<H1>
	Title
	</H1> '''

#Ejemplo 2 (con contextmanager)
	import contextlib
	import time

	@contextlib.contextmanager # [ ] generador de contexto  
	def stopwatch(message):
	    """Administrador de contexto para imprimir cuánto tiempo tomó un bloque de código.
	    devuelve 'message más el tiempo empleado."""
	    t0 = time.time()
	    try:
	        yield # diferente a return, ya que devuelve generadores.
	    finally:
	        t1 = time.time()
	        print('Total elapsed time for %s: %.3f' % (message, t1 - t0))

	with stopwatch('prueba'): # con decorador stopwatch, ejecutar:
	    print ("Probando generador de contexto")
	    time.sleep(2) # para dos segundos
	    print('Finalizado...')
	'''
	genera:
	Probando generador de contexto
	Finalizado...
	Total elapsed time for prueba: 2.012 '''

# Comparando un decorador con un gestor de contextos (contextlib.contextmanager):

	# decorador.
	def main():
	    func_error()

	def decorador(func):
	    def mierror(**kwargs):
	        try:
	            func(**kwargs)
	        except Exception as er:
	            print ("Ha habido un error de tipo %s" %er)
	    return mierror

	@decorador
	def func_ok():
	    print ("Funcionamiento correcto")

	@decorador
	def func_error():
	    raise KeyError("función fallando")
	    print("Pasando de todo") # esto no se ejecuta porque el código se interrumpe.


	if __name__ == '__main__':
	    main()


	# con contextmanager

	import contextlib

	def main():
	    func_error()

	def func_ok():
	    with mierror("función func_ok"):
	        print ("Funcionamiento correcto")

	def func_error():
	    with mierror("función: func_error"):
	        raise KeyError("función fallando") # esto se queda dentro del bloque y el código continúa.
	    print("Pasando de todo") # esto, a diferencia del anterior, sí que se ejecuta.

	@contextlib.contextmanager
	def mierror(mensaje):
	    try:
	        yield
	    except Exception as er:
	        print ("Ha habido un error de tipo %s en %s" % (er,mensaje))

	if __name__ == '__main__':
	    main()
