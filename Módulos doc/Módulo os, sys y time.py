# Uso de los módulos os, sys y time

# Resumen de varias funcioones:

import os, sys, time
os.access(ruta, modo-acceso)  # devuelve si se puede acceder a un archivo o directorio
os.getcwd()  # devuelve el directorio de trabajo
os.chdir('/dir1/dir2')  # cambia directorio trabajo
os.chmod(path, mode)  # cambia permisos a un archivo
os.chown(path, uid, gid)  # cambia propietario de un archivo 
os.chroot(path)  # cambia al directorio de trabajo raíz
os.cpu_count() # número de CPUs del sistema
os.curdir  #  directorio actual
os.pardir #  directorio padre
os.ctermid()  # nombre del archivo del terminal
os.devnull  # ruta del dispositivo nulo
os.environ.iteritems()  # diccionario con variables de entorno y valor
os.getuid()  # devuelve id usuario real del proceso actual (Unix)
os.getgid()  # devuelve id grupo real del proceso actual (Unix)
os.geteuid()  # devuelve id usuario efectivo del proceso actual (Unix)
os.getegid()  # devuelve id grupo efectivo del proceso actual (Unix)
os.getgroups()  # devuelve lista de grupos suplementarios relacionados con el proceso actual (Unix)
os.getpid()  # devuelve id del proceso actual
os.getenv(key, default=None)  # obtiene valor de variable de entorno
os.getlogin()  # devuelve nombre usuario actual
listado = os.listdir('/home')  # lista contenido de directorio
os.mkdir(path [,mode=511])  # crea subdirectorio
os.makedirs(path[, modo])  # crea directorios recursivamente
os.path.abspath(path)  # devuelve path absoluta de un archivo o directorio
os.path.abspath(__file__)  # devuelve ruta completa del fichero actual
os.path.basename(path)  # devuelve directorio base
os.path.dirname(path)  # devuelve directorio del archivo o directorio
os.path.exists(path)  # comprueba si existe fichero o directorio
os.path.expanduser('~') # devuelve directorio de usuario.
os.path.getatime(path)  # devuelve fecha/hora del último acceso a un archivo o directorio
os.path.getsize(path)  # obtiene el tamaño de un archivo o directorio
os.path.isabs(path)  # devuelve si la ruta es absoluta
os.path.isfile(path)  # devuelve si la ruta es un archivo
os.path.isdir(path)  # devuelve si la ruta es un directorio
os.path.islink(path)  # devuelve si la ruta es un enlace simbólico
os.path.ismount(path)  # devuelve si la ruta es un punto de montaje
os.putenv(key, value)  # cambia/inserta variable de entorno
os.remove(path)  # borra un archivo
os.removedirs(path)  # elimina directorios recursivamente
os.rename(old, new)  # renombrar un archivo o directorio
os.renames(old, new)  # Renombrado recursivo.
os.rmdir(path)  # borrar un subdirectorio
os.link(src, dst)  # crea enlace duro
os.symlink(path, nombre-destino)  # crea enlace simbólico
os.readlink(path)  # cadena que representa ruta a la que apunta enlace simbólico
os.stat(path)  # Estado de archivo o de descriptor de archivo.
os.sep  # separador utilizado en una ruta (path)
os.extsep  # separador de extensión
os.linesep  # separador de líneas
os.pathsep  # separador usado para expresar varias rutas
os.system('ls')  # ejecuta un comando externo
os.uname()  # muestra Información del sistema. Tiene 5 atributos 
os.uname().sysname  # muestra nombre del sistema. Otros atributos: nodename, release, version y machine
os.unsetenv(key)  # borra una variable de entorno
os.urandom(n)  # genera cadenas aleatorias de n bytes
os.wait()  # espera fin de un proceso hijo y devuelve tupla con estado pid y salida (unix)
sys.argv  # devuelve la lista formada por programa y lista de argumentos agregados al ejecutar
sys.executable  # devuelve ruta del ejecutable del intérprete
sys.exit()  # fuerza salida del intérprete Python, retornando un valor de salida para saber el motivo.
sys.getdefaultencoding()  # devuelve codificación de caracteres por defecto
sys.getfilesystemencoding()  # devuelve codificación de caracteres que se utiliza para convertir los nombres de archivos unicode en nombres de archivos del sistema
sys.path  # devuelve paths de Python
sys.path.append('ruta')  # añade una nueva ruta al path
sys.modules  # muestra información de los módulos
sys.stdout.write   # Muestra en salida estandar (pantalla normalmente)
sys.version  # obtiene versión de Python
sys.copyright  # obtiene información de copyright
sys.platform  # obtiene sistema operativo del sistema
sys.version_info  # obtiene información de versión
sys.version_info.major >= 3  # obtiene versión major
time.time()  # hora actual en segundos (coma flotante)
time.ctime()  # convierte de segundos a cadena
time.localtime()  # muestra hora local como tupla
time.asctime()  # convierte fecha y hora locales a cadena
time.sleep()  # retarda ejecución un número de segundos
fecha = datetime.datetime.strptime(fecha, "%d-%m-%Y") # valida dato input como fecha