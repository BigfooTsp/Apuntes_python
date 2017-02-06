-----INVOCAR MÉTODOS DE OTRAS CLASES:-----

	> Si solicitas un método de clase sin instanciar la clase, recibes un name 'self' is no defined.
	> En el mismo módulo, para invocar un metodo de una clase desde el método de otra, usar (self) también.
		
			def metodo2(self):
					print("Esto es método2()")
					clase2.metodo3(self) # este self

		class clase2():
			def metodo3(self):
				print ("Esto es metodo3()")

		Si la clase estuviera dentro de la propia clase, debería ser:

			self.clase2.metodo3(self) # este self

	> Sin embargo, para invocar un método de una clase desde fuera de esta, se debe de importar o/e instanciar.