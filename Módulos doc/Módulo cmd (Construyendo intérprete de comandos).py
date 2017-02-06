'''
Construir un intérprete de comandos con librería CMD.

http://python-para-impacientes.blogspot.com.es/2016/07/cmd-construyendo-un-interprete-de.html
https://docs.python.org/3/library/cmd.html
https://wiki.python.org/moin/CmdModule

Para colores en consola ver módulo colorama:
http://python-para-impacientes.blogspot.com.es/2016/09/dar-color-las-salidas-en-la-consola.html
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
'''
Control + P  retrocede al comando anterior,
Control + N  avanza al comando siguiente,
Control + F  mueve cursor a derecha (sin borrado),
Control + B  mueve cursor a izquierda (sin borrado), etc.
TAB muestra autocompletado de comandos.
HELP o ? muestra ayuda, 'help comando' ayuda de comando, help_comando(sin do_)

Con help o ? se muestra la ayuda del intérprete. help 'comando' muestra la ayuda del comando.

! llama al método do_shell() si está definido.

Atributos de la clase Cmd:
Cmd.identchars. Define cadena con los caracteres que se pueden utilizar en la escritura de comandos.
Cmd.intro. El texto asignado es utilizado para mostrar un mensaje inicial.
Cmd.lastcmd. El comando asignado se ejecutará cuando se presione la tecla [Return] si previamente 
			 no se introdujo uno válido.
Cmd.prompt. El texto asignado se mostrará en el lugar donde se introducen los comandos.
Cmd.doc_header: Cabecera a mostrar si la ayuda tiene una sección de comandos documentados.
Cmd.misc_header. Cabecera a mostrar si la ayuda tiene una sección miscelánea. La sección miscelánea 
			     la constituyen otros métodos distintos a los do_*() que tienen su correspondientes 
			     métodos de ayuda help_*().
Cmd.undoc_header. Cabecera a mostrar si la ayuda tiene una sección de comandos no documentados.
Cmd.ruler. Carácter para subrayar los encabezados. Por defecto, es el signo "="
'''
 
import cmd
import os
 
class Comandos(cmd.Cmd):
    """Interprete de comandos"""
    prompt = "Introduza un comando: "
    identchars = "comandoslirhep123"
    lastcmd = "comando2"
    intro = "Hola, buenos dias"
    doc_header = "Ayuda de comandos documentados"
    undoc_header = "Ayuda de comandos no documentados"
    misc_header = "Ayuda de otros metodos"
    ruler = "-"   

    # Comandos:
             
    def do_comando1(self, args): # do_ para definir un comando
        """Ayuda del comando1"""
        print("comando1 se ha ejecutado")
 
    def do_comando2(self, args):
        """Ayuda del comando2"""
        print("comando2 se ha ejecutado")

    def do_comando3(self, args):
        """Ayuda del comando3: ejecuta comando1 y comando2"""
        self.onecmd("comando1")
        self.onecmd("comando2")

    # Ejemplo de comandos con argumentos:

    def do_suma(self, args):
        """Suma los argumentos que sean enteros. Ej.: suma 12 13"""
        enteros = obtener_enteros(args)
        if len(enteros) > 1:
            print('Total', sum(enteros))
        else:
            print('La operación requiere al menos dos números enteros')

    def obtener_enteros(args):
        """Los argumentos se deben escribir a continuación del comando separados por espacios en blanco. 
        Cuando la lista de argumentos se analice, se extraerán de ella los números enteros y 
        se omitirá otro tipo de información (cadenas, números con decimales y otros caracteres). """
        argumentos = args.split()
        enteros = list(filter(lambda x: x.isnumeric(), argumentos))
        enteros = list(map(int,enteros))
        return(enteros)

    # Configurando comportamiento de consola.

    def do_salir(self, args):
        """Salir del interprete"""
        print("Hasta pronto")
        return(True)

    ''' Se pueden configurar otros métodos diferentes de do_ , para implementar
        su ayuda se requiere otro método con nombre help_comando '''

    def do_help(self, args): # Configura ayuda, anulando la que viene por defecto.
        print("Ayuda")

    def emptyline(self): # configura linea vacía, por defecto repite último comando.
        """No realiza ninguna accion"""
        pass

    def default(self, args): # Configura comando erroneo.
        print("Error. Comando no reconocido:", args)

    def precmd(self, args): # Configura antes de comando
        args = args.lower() # en este caso, pasa el comando a minúsculas.
        return(args)
 
    def postcmd(self, stop, args): # Configura después de comando.
        '''Es llamado después de la ejecución del método de un comando. Utiliza la bandera stop para controlar
         si la ejecución se dará por terminada después de la llamada a postcmd(), 
         siendo también el valor de retorno del método onecmd(). En el ejemplo se utiliza para recordar 
         que el comando salir finaliza la ejecución del intérprete.'''            
        if args == "salir":            
            stop = True       
        else:
            print("Para finalizar introducir 'salir'")            
            stop = False
        return(stop)

    def preloop(self): # configura inicio del bucle
        '''La sesion de trabajo ha comenzado'''
        print("La sesion de trabajo ha comenzado")
         
    def postloop(self): # Configura final del bucle
        '''La sesion de trabajo ha finalizado'''
        print("La sesion de trabajo ha finalizado")

    def do_shell(self, s):
        ''' Ejecuta comandos en shell. Atajo mediante '!' '''
        os.system(s)
     
 
if __name__ == '__main__':
    interprete = Comandos()
    interprete.cmdloop(intro="Bienvenido") # Inicia el loop con mensaje de bienvenida. 
                                            #Cmd.cmdloop(intro=None), return(True) para cerrar bucle.

