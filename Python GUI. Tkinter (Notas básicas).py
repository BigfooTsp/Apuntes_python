# MANEJO DE LA LIBRERÍA TKINTER PARA INTERFACES GRÁFICAS EN PYTHON

# ESTRUCTURA BÁSICA
	from tkinter import *

	interface = Tk()

	 # Aquí iría el desarrollo del programa

	interface.mainloop()


# EJEMPLO CON PROGRAMA CONVERSIÓN DE DIVISAS

	from tkinter import *

	interfaz=Tk()

	def convertir():
	    cPeso=dolares.get()*pDolar.get()
	    messagebox.showinfo(title="Ejercicio 4",message=str(dolares.get())+" dólares equivalen a "+str(cPeso)+" pesos")

	interfaz.geometry("500x300+100+100")
	interfaz.title("Ejercicio 4")
	lblTitle=Label(text="***CONVERSOR DÓLARES A PESOS***",font=("AR CENA",14)).pack()

	lblpDolar=Label(text="Ingrese el precio actual del dólar: ",font=("Agency FB",14)).place(x=10,y=40)
	pDolar=DoubleVar()
	txtIngrese=Entry(interfaz,textvariable=pDolar).place(x=270,y=48)

	lblDolares=Label(text="Ingrese la cantidad de dólares a convertir: ",font=("Agency FB",14)).place(x=10,y=70)
	dolares=DoubleVar()
	txtIngrese=Entry(interfaz,textvariable=dolares).place(x=270,y=78)

	btnResultado=Button(interfaz,text="Convertir",command=convertir,font=("Agency FB",14)).place(x=10,y=110)

	interfaz.mainloop()