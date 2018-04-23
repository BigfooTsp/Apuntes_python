#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

# Calcula coste de viaje con validación y cálculo inmediato

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Alta Velocidad")
        
        # Declara variables de control
                                   
        self.num_via = IntVar(value=1)
        self.ida_vue = BooleanVar()        
        self.clase   = StringVar(value='t')
        self.km = IntVar(value=1)        
        self.precio = DoubleVar(value=0.10)
        self.total = DoubleVar(value=0.0)
        
        # Define trazas con variables de control de los widgets Entry()
        # para detectar cambios en los datos. Si se producen cambios
        # se llama a la función 'self.calcular' para validación y para
        # calcular importe a pagar
        
        self.km.trace('w', self.calcular)
        self.precio.trace('w', self.calcular)
        
        # Llama a función para validar y calcular
        
        self.calcular()
        
        # Carga imagen para asociar a widget Label()
                
        tren = PhotoImage(file='tren-128x64.png')  
        
        # Declara widgets de la ventana
        # En los widgets de tipo Spinbox, Checkbutton y Radiobutton
        # se utiliza la opción 'command' para llamar a la función 
        # 'self.calcular' para validar datos y calcular importe a 
        # pagar de forma inmediata
              
        self.imagen1 = ttk.Label(self.raiz, image=tren, 
                                 anchor="center")
        self.etiq1 = ttk.Label(self.raiz, text="Viajeros:")                               
        self.viaje = Spinbox(self.raiz, from_=1, to=20, wrap=True,
                             textvariable=self.num_via, 
                             state='readonly',
                             command=self.calcular)                                                              
        self.idavue = ttk.Checkbutton(self.raiz, text='Ida y vuelta', 
                                      variable=self.ida_vue, 
                                      onvalue=True, offvalue=False, 
                                      command=self.calcular)
        self.etiq2 = ttk.Label(self.raiz, text="Clase:")
        self.clase1 = ttk.Radiobutton(self.raiz, text='Turista', 
                                      variable=self.clase, value='t',
                                      command=self.calcular)
        self.clase2 = ttk.Radiobutton(self.raiz, text='Primera', 
                                      variable=self.clase, value='p',
                                      command=self.calcular)
        self.clase3 = ttk.Radiobutton(self.raiz, text='Lujo', 
                                      variable=self.clase, value='l',
                                      command=self.calcular)        
        self.etiq3 = ttk.Label(self.raiz, 
                               text="Distancia (Kilómetros):")
        self.dist = ttk.Entry(self.raiz, textvariable=self.km, 
                              width=10)                
        self.etiq4 = ttk.Label(self.raiz, text="Precio:")
        self.coste = ttk.Entry(self.raiz, textvariable=self.precio, 
                               width=10)        
        self.etiq5 = ttk.Label(self.raiz, text="A Pagar (euros):")        
        self.etiq6 = ttk.Label(self.raiz, textvariable=self.total,
                               foreground="yellow", background="black",
                               borderwidth=5, anchor="e")                                
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
                
        self.boton1 = ttk.Button(self.raiz, text="Salir", 
                                 command=quit)                                 
                                                     
        self.imagen1.pack(side=TOP, fill=BOTH, expand=True, 
                          padx=10, pady=5)
        self.etiq1.pack(side=TOP, fill=BOTH, expand=True, 
                        padx=10, pady=5)
        self.viaje.pack(side=TOP, fill=X, expand=True, 
                        padx=20, pady=5)
        self.idavue.pack(side=TOP, fill=X, expand=True, 
                         padx=20, pady=5)
        self.etiq2.pack(side=TOP, fill=BOTH, expand=True, 
                        padx=10, pady=5)
        self.clase1.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=20, pady=5)
        self.clase2.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=20, pady=5)
        self.clase3.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=20, pady=5)
        self.etiq3.pack(side=TOP, fill=BOTH, expand=True, 
                        padx=10, pady=5)
        self.dist.pack(side=TOP, fill=X, expand=True, 
                       padx=20, pady=5)
        self.etiq4.pack(side=TOP, fill=BOTH, expand=True, 
                        padx=10, pady=5)
        self.coste.pack(side=TOP, fill=X, expand=True, 
                        padx=20, pady=5)
        self.etiq5.pack(side=TOP, fill=BOTH, expand=True, 
                        padx=10, pady=5)
        self.etiq6.pack(side=TOP, fill=BOTH, expand=True, 
                        padx=20, pady=5)        
        self.separ1.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        self.boton1.pack(side=RIGHT, fill=BOTH, expand=True, 
                         padx=10, pady=10)
        self.raiz.mainloop()
        
    def calcular(self, *args):
        
        # Función para validar datos y calcular importe a pagar
        
        error_dato = False
        total = 0
        try:
            km = int(self.km.get())
            precio = float(self.precio.get())
        except:
            error_dato = True    
        if not error_dato:
            total =  self.num_via.get() * km * precio
            if self.ida_vue.get():
                total = total * 1.5
            if self.clase.get() == 'p':
                total = total * 1.2
            elif self.clase.get() == 'l':
                total = total * 2
            self.total.set(total)                
        else:
            self.total.set("¡ERROR!")
            
def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()