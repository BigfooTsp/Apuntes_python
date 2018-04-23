#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:        pyremoto.py (Python 3.x).
# description: Acceso Remoto a equipos por ssh, sftp y rdp
# purpose:     Construcción de menús, barras de herramientas
#              y de estado 
# author:      python para impacientes
#
#------------------------------------------------------------

'''PyRemoto: Acceso Remoto a equipos por ssh, sftp y rdp '''
   
__author__ = 'python para impacientes'
__title__= 'PyRemoto'
__date__ = ''
__version__ = '0.0.1'
__license__ = 'GNU GPLv3'

import os, sys, webbrowser, platform
from tkinter import *
from tkinter import ttk, font, messagebox   # ttk para nuevos elementos de últimas versiones de tkinter.

# PYREMOTO: ACCESO REMOTO A EQUIPOS POR SSH, SFTP y RDP

class PyRemoto():
    ''' Clase PyRemoto '''
    
    # DECLARAR MÉTODO CONSTRUCTOR DE LA APLICACIÓN
        
    def __init__(self, img_carpeta, iconos):                      
        ''' Definir ventana de la aplicación, menú, submenús, 
            menú contextual, barra de herramientas, barra de
            estado y atajos del teclado '''
        
        # INICIALIZAR VARIABLES
        
        self.img_carpeta = img_carpeta
        self.iconos = iconos
                
        # DEFINIR VENTANA DE LA APLICACIÓN:
        
        self.raiz = Tk()
        
        # ESTABLECER PROPIEDADES DE LA VENTANA DE APLICACIÓN:
        
        self.raiz.title("PyRemoto " + __version__)  # Título
        self.icono1= PhotoImage(file=self.iconos[0])  # Icono app
        self.raiz.iconphoto(self.raiz, self.icono1)  # Asigna icono app 
        self.raiz.option_add("*Font", "Helvetica 12")  # Fuente predeterminada        
        self.raiz.option_add('*tearOff', False)  # Deshabilita submenús flotantes
        self.raiz.attributes('-fullscreen', True)  # Maximiza ventana completa        
        self.raiz.minsize(400,300)  # Establece tamaño minimo ventana
        
        # ESTABLECER ESTILO FUENTE PARA ALGUNOS WIDGETS:
        
        self.fuente = font.Font(weight='normal') # normal, bold, etc...

        # DECLARAR VARIABLES PARA OPCIONES PREDETERMINADAS:
        # (Estos valores se podrían leer de un archivo de
        # configuración)
        
        self.CFG_TIPOCONEX = IntVar()
        self.CFG_TIPOCONEX.set(1) # shh
        self.CFG_TIPOEMUT = IntVar()
        self.CFG_TIPOEMUT.set(1) # xterm
        self.CFG_TIPOEXP = IntVar()
        self.CFG_TIPOEXP.set(1) # thunar
        
        # DECLARAR VARIABLE PARA MOSTRAR BARRA DE ESTADO:
        
        self.estado = IntVar()
        self.estado.set(1)  # Mostrar Barra de Estado
                         
        # DEFINIR BARRA DE MENÚ DE LA APLICACION:
        
        barramenu = Menu(self.raiz)
        self.raiz['menu'] = barramenu

        # DEFINIR SUBMENÚS 'Sesiones', 'Opciones' y 'Ayuda':

        menu1 = Menu(barramenu)
        self.menu2 = Menu(barramenu)
        menu3 = Menu(barramenu)
        barramenu.add_cascade(menu=menu1, label='Sesiones')
        barramenu.add_cascade(menu=self.menu2, label='Opciones')
        barramenu.add_cascade(menu=menu3, label='Ayuda')

        # DEFINIR SUBMENÚ 'Sesiones':

        icono2 = PhotoImage(file=self.iconos[1])
        icono3 = PhotoImage(file=self.iconos[2])

        menu1.add_command(label='Conectar...', 
                          command=self.f_conectar, 
                          underline=0, accelerator="Ctrl+c",
                          image=icono2, compound=LEFT)
        menu1.add_separator()  # Agrega un separador
        menu1.add_command(label='Salir', command=self.f_salir, 
                          underline=0, accelerator="Ctrl+q",
                          image=icono3, compound=LEFT)

        # DEFINIR SUBMENÚ 'Opciones':
                
        self.menu2.add_checkbutton(label='Barra de Estado', 
                          variable=self.estado, onvalue=1, 
                          offvalue=0, 
                          command=self.f_verestado)
        self.menu2.add_separator()
        self.menu2.add_radiobutton(label='ssh', 
                          variable=self.CFG_TIPOCONEX,
                          command=self.f_cambiaropc,
                          value=1)
        self.menu2.add_radiobutton(label='sftp',
                          variable=self.CFG_TIPOCONEX,
                          command=self.f_cambiaropc,
                          value=2)
        self.menu2.add_radiobutton(label='rdp',
                          variable=self.CFG_TIPOCONEX,
                          command=self.f_cambiaropc,
                          value=3)
        self.menu2.add_separator()
        self.menu2.add_radiobutton(label='xterm', 
                          variable=self.CFG_TIPOEMUT, 
                          command=self.f_cambiaropc, 
                          value=1)
        self.menu2.add_radiobutton(label='uxterm', 
                          variable=self.CFG_TIPOEMUT, 
                          command=self.f_cambiaropc,
                          value=2)
        self.menu2.add_radiobutton(label='xfce4-terminal', 
                          variable=self.CFG_TIPOEMUT, 
                          command=self.f_cambiaropc, 
                          value=3)
        self.menu2.add_separator()
        self.menu2.add_radiobutton(label='Thunar', 
                          variable=self.CFG_TIPOEXP, 
                          command=self.f_cambiaropc, 
                          value=1)
        self.menu2.add_radiobutton(label='Nautilus', 
                          variable=self.CFG_TIPOEXP, 
                          command=self.f_cambiaropc, 
                          value=2)
        self.menu2.add_separator()
        self.menu2.add_command(label='Guardar', 
                          command=self.f_opcionguardar,
                          state="disabled", underline=0,
                          accelerator="Ctrl+g")    

        # DEFINIR SUBMENÚ 'Ayuda':

        menu3.add_command(label='Web', command=self.f_web)
        menu3.add_command(label='Atajos teclado', 
                          command=self.f_atajos)      
        icono4 = PhotoImage(file=self.iconos[3])
        menu3.add_command(label="Acerca de", 
                          command=self.f_acerca,
                          image=icono4, compound=LEFT)

        # DEFINIR BARRA DE HERRAMIENTAS:

        self.icono5 = PhotoImage(file=self.iconos[4])
        icono6 = PhotoImage(file=self.iconos[5])

        barraherr = Frame(self.raiz, relief=RAISED,
                          bd=2, bg="#E5E5E5")
        bot1 = Button(barraherr, image=self.icono5, 
                      command=self.f_conectar)
        bot1.pack(side=LEFT, padx=1, pady=1)
        bot2 = Button(barraherr, image=icono6, 
                      command=self.f_salir)
        bot2.pack(side=LEFT, padx=1, pady=1)
        barraherr.pack(side=TOP, fill=X)
                
        # DEFINIR BARRA DE ESTADO:
        # Muestra información del equipo
        
        info1 = platform.system()
        info2 = platform.node()
        info3 = platform.machine()
        
        # Otro modo de obtener la información: 
        # (No disponible en algunas versiones de Windows)
        
        #info1 = os.uname().sysname
        #info2 = os.uname().nodename
        #info3 = os.uname().machine
     
        mensaje = " " + info1+ ": "+info2+" - "+info3
        self.barraest = Label(self.raiz, text=mensaje, 
                              bd=1, relief=SUNKEN, anchor=W)
        self.barraest.pack(side=BOTTOM, fill=X)

        # DEFINIR MENU CONTEXTUAL

        self.menucontext = Menu(self.raiz, tearoff=0)
        self.menucontext.add_command(label="Conectar", 
                                     command=self.f_conectar)
        self.menucontext.add_command(label="Salir", 
                                     command=self.f_salir)

        # DECLARAR TECLAS DE ACCESO RAPIDO:
        
        self.raiz.bind("<Control-c>", 
                       lambda event: self.f_conectar())
        self.raiz.bind("<Control-g>", 
                       lambda event: self.f_guardar())
        self.raiz.bind("<Control-q>", 
                       lambda event: self.f_salir())
        self.raiz.bind("<Button-3>", 
                       self.f_mostrarmenucontext)
        self.raiz.mainloop()
        
    # DECLARAR OTROS MÉTODOS DE LA APLICACIÓN:

    def f_opcionguardar(self):
        ''' Si opción 'Guardar' está habilitada llama a
            método para guardar opciones de configuración
            de la aplicación '''
            
        if self.menu2.entrycget(13,"state")=="normal":            
            self.menu2.entryconfig(13, state="disabled")
            self.f_guardarconfig()

    def f_guardarconfig(self):
        ''' Guardar opciones de configuración de la aplicación '''
        print("Configuración guardada")
                                                    
    def f_conectar(self):
        ''' Definir ventana de diálogo para conectar con equipos '''
        print("Conectando")
          
    def f_cambiaropc(self):
        ''' Habilitar opción 'Guardar' al elegir alguna opción
            de tipo de conexión, emulador de terminar o 
            explorador de archivos '''            
        self.menu2.entryconfig("Guardar", state="normal")
                    
    def f_verestado(self):
        ''' Ocultar o Mostrar barra de estado '''
        
        if self.estado.get() == 0:
            self.barraest.pack_forget()
        else:
            self.barraest.pack(side=BOTTOM, fill=X)
    
    def f_mostrarmenucontext(self, e):
        ''' Mostrar menú contextual '''
        self.menucontext.post(e.x_root, e.y_root)
        
    def f_web(self):
        ''' Abrir página web en navegador Internet '''
        
        pag1 = 'http://python-para-impacientes.blogspot.com/'
        webbrowser.open_new_tab(pag1)
    
    def f_atajos(self):
        ''' Definir ventana de diálogo con lista de 
            combinaciones de teclas de la aplicación '''
        pass
            
    def f_acerca(self):
        ''' Definir ventana de diálogo 'Acerca de' '''
        
        acerca = Toplevel()
        acerca.geometry("320x200")
        acerca.resizable(width=False, height=False)
        acerca.title("Acerca de")
        marco1 = ttk.Frame(acerca, padding=(10, 10, 10, 10),
                           relief=RAISED)
        marco1.pack(side=TOP, fill=BOTH, expand=True)
        etiq1 = Label(marco1, image=self.icono5, 
                      relief='raised')
        etiq1.pack(side=TOP, padx=10, pady=10, 
                   ipadx=10, ipady=10)
        etiq2 = Label(marco1, text="PyRemoto "+__version__, 
                      foreground='blue', font=self.fuente)
        etiq2.pack(side=TOP, padx=10)
        etiq3 = Label(marco1, 
                      text="Python para impacientes")
        etiq3.pack(side=TOP, padx=10)
        boton1 = Button(marco1, text="Salir", 
                        command=acerca.destroy)
        boton1.pack(side=TOP, padx=10, pady=10)
        boton1.focus_set()
        acerca.transient(self.raiz)
        self.raiz.wait_window(acerca)
        
    def f_salir(self):
        ''' Salir de la aplicación '''
        self.raiz.destroy()

# FUNCIONES DE LA APLICACIÓN
          
def f_verificar_iconos(iconos):
    ''' Verifica existencia de iconos
    
    iconos -- Lista de iconos '''        
    
    for icono in iconos:
        if not os.path.exists(icono):
            print('Icono no encontrado:', icono)
            return(1)
    return(0)

def main():
    ''' Iniciar aplicación '''
    
    # INICIALIZAR VARIABLES CON RUTAS
    
    app_carpeta = os.getcwd()
    img_carpeta = app_carpeta + os.sep + "imagen" + os.sep
       
    # DECLARAR Y VERIFICAR ICONOS DE LA APLICACIÓN:

    iconos = (img_carpeta + "pyremoto64x64.png",
              img_carpeta + "conec16x16.png",
              img_carpeta + "salir16x16.png",
              img_carpeta + "star16x16.png",
              img_carpeta + "conec32x32.png",
              img_carpeta + "salir32x32.png")                  
    error1 = f_verificar_iconos(iconos)
       
    if not error1:
        mi_app = PyRemoto(img_carpeta, iconos)
    return(0)

if __name__ == '__main__':
    main()