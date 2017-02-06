# Plantilla para  consola de comandos con modulos cmd y colorama.

'''
Instrucciones:
# Colorama:
	el módulo con init(autoreset=True) en lugar de init().
	Estilos*	(Style)
		Débil	DIM
		Normal	NORMAL
		Brillante	BRIGHT
		Reset	RESET_ALL
	Colores Texto/Fondo	(Fore/Back)
		Negro	BLACK
		Rojo	RED
		Verde	GREEN
		Amarillo	YELLOW
		Azul	BLUE
		Morado	MAGENTA
		Cian	CYAN
		Blanco	WHITE
		Reset	RESET
        ej: print(Fore.RED + Style.DIM + "texto")

	Movimiento del cursor:
		Cursor.POS(columna, fila): desplaza el cursor a la fila y columna indicadas.
		Cursor.UP(número): desplaza el cursor a la línea anterior. 
		Cursor.DOWN(número): desplaza el cursor a la línea siguiente. 
		Cursor.FORWARD(número): avanza el cursor un número de caracteres en la línea actual.
		Cursor.BACK(número): retrocede el cursor un número de caracteres en la línea actual.
# cmd.CMD
	Control + P  retrocede al comando anterior,
	Control + N  avanza al comando siguiente,
	Control + F  mueve cursor a derecha (sin borrado),
	Control + B  mueve cursor a izquierda (sin borrado), etc.
	TAB muestra autocompletado de comandos.
	HELP o ? muestra ayuda, 'help comando' ayuda de comando, help_comando(sin do_)
    shell o ! para introducir comando de sistema.
'''

import cmd
from colorama import init, Fore, Back, Style, Cursor
import sys
import os
import contextlib

# Configuro colorama
init(autoreset=True) # configurado para que se resetee colorama a cada uso.
Rojo = (Fore.RED + Style.BRIGHT)
RojoLeve = (Fore.RED + Style.DIM)
Amarillo = (Fore.YELLOW + Style.BRIGHT)


class Comandos(cmd.Cmd):
    """Interprete de comandos"""
    prompt = (Fore.GREEN + Style.BRIGHT + "comando >> ")
    #identchars = ""
    #lastcmd = ""
    intro = ""
    doc_header = (Amarillo + "Ayuda de comandos documentados")
    undoc_header = (Amarillo + "Ayuda de comandos no documentados")
    misc_header = (Amarillo + "Ayuda de otros metodos")
    ruler = (Fore.BLUE + "-")  

    ############################### LISTA DE COMANDOS ####################################


         
    def do_comando1(self, args): # do_ para definir un comando
        """Ayuda del comando1"""
        with consoleError("Comando 1"): # Para controlar error en @contextmanager
            print("comando1 se ha ejecutado")
 
    def do_comando2(self, args):
        """Ayuda del comando2"""
        print("comando2 se ha ejecutado")

    def do_comando3(self, args):
        """Ayuda del comando3: ejecuta comando1 y comando2"""
        self.onecmd("comando1")
        self.onecmd("comando2")
    

    ''' Se pueden configurar otros métodos diferentes de do_ , para implementar
        su ayuda se requiere otro método con nombre help_comando '''



    ############################### CONFIGURANDO CONSOLA ####################################
    def do_salir(self, args):
    	'Salir del programa'
    	return(True) # devuelve true al loop para cerrarlo.

    def do_clear(self, args):
    	'''Limpia la pantalla '''
    	self.preloop() # Inicia pantalla de presentación.

    def default(self, args): # Configura comando erroneo.
        print(Fore.RED + Style.DIM + "Error: Comando '%s' no reconocido:\n'help' si necesitas ayuda"%args)

    def precmd(self, args): # Configura antes de comando
        args = args.lower() # en este caso, pasa el comando a minúsculas.
        return(args)

    def emptyline(self): # configura linea vacía, por defecto repite último comando.
        """No realiza ninguna accion"""
        pass

    #def do_help(self, args): # Configura ayuda, anulando la que viene por defecto.
    #    None

    def postcmd(self, stop, args): # Configura después de comando.
        '''Es llamado después de la ejecución del método de un comando. Utiliza la bandera stop para controlar
         si la ejecución se dará por terminada después de la llamada a postcmd(), 
         siendo también el valor de retorno del método onecmd(). En el ejemplo se utiliza para recordar 
         que el comando salir finaliza la ejecución del intérprete.'''            
        if args == "salir":
        	stop = True       
        else:
            #print(Fore.YELLOW + Style.DIM + "Para finalizar introducir 'salir'")            
            stop = False
        return(stop)

    def preloop(self): # configura inicio del bucle
        '''La sesion de trabajo ha comenzado'''
        if os.name=="posix": os.system ("clear")
        elif os.name == ("ce", "nt", "dos"): os.system ("cls")

        # TÍTULO DE LA CONSOLA
        print(Cursor.POS(1,1) + ROJO + 
        	"                            CONSOLA               ")
         
    def postloop(self): # Configura final del bucle
        '''La sesion de trabajo ha finalizado'''
        print(Fore.RED + "\nLa sesion ha finalizado...")

    def do_shell(self, s):
        ''' ejecuta comando de sistema. Atajo de acceso '!' '''
        os.system(s)

@contextlib.contextmanager # Control de errores.
def consoleError(mensaje):
    try:
        yield
    except Exception as er:
        print (Fore.RED + Style.BRIGHT + "Error en comando '%s' de tipo:\n%s" %(mensaje, er))




 
if __name__ == '__main__':
	consola = Comandos()
	consola.cmdloop() # Inicia el loop con mensaje de bienvenida.
