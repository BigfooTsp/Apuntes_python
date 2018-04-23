os.path.abspath(path) 
#Devuelve la ruta absoluta al archivo, hace lo mismo que: normpath(join(os.getcwd(), path)).

os.path.basename(path) 
#Devuelve el nombre del archivo.

os.path.commonprefix(list) 
#Devuelve el prefijo de ruta más larga tomado caracater por caracter.

os.path.dirname(path) 
#Devuelve el directorio de un archivo. Corresponde al primer valor de la pareja regrsada por split(path)

os.path.exists(path) 
#Devuelve true si la ruta existe.

os.path.lexists(path) 
#Igual al anterior.

os.path.expanduser(path) 
#Devuelve el argumento con un componente inicial ~ o ~user.

os.path.expandvars(path) 
#Regresa el argumento con las variables de entorno ampliado.

os.path.getatime(path) 
#Segundos desde el ultimo acceso a la dirección.

os.path.getmtime(path) 
#Segundos desde la ultima modificación.

os.path.getctime(path) 
#Igual al anterior.

os.path.getsize(path) 
#Tamaño en bytes.

os.path.isabs(path) 
#Devuelve true si es una ruta absoluta.

os.path.isfile(path) 
#True si path es un archivo.

os.path.isdir(path) 
#True si path es un directorio.

os.path.islink(path) 
#True si path es un enlace simbólico.

os.path.ismount(path) 
#True si path es una ruta de montaje verdadea.

os.path.join(path1[, path2[, ...]]) 
#Une 2 rutas de manera inteligente. Retorna el valor de unir las rutas con separador os.sep 

os.path.normcase(path) 
#Normaliza la ruta (las pone en minusculas, invierte los separadores, etc.)

os.path.normpath(path) 
#Similar al anterior.

os.path.realpath(path) 
#Retorna Canonicalpath.

os.path.relpath(path[, start]) 
#Devuelve una ruta relativa al directorio actual o al elegido en start. (start defaults to os.curdir)

os.path.samefile(path1, path2) 
#Devuelve true si ambos argumentos se refieren a la misma direccion de archivo o directorio.

os.path.sameopenfile(fp1, fp2) 
#True si ambos parametros refieren a un mismo archivo.

os.path.samestat(stat1, stat2) 
#True si ambos stat refieren a un mismo archivo.

os.path.split(path) 
#Devuelve una pareaja (head, tail) que contiene el directorio y el archivo segun path.

os.path.splitdrive(path) 
#Devuelve una pareja (drive, tail) donde drive es la unidad y tail la direccion a partir de ella.

os.path.splitext(path) 
#Devuelve un par (root, ext). Raiz mas path.

os.path.splitunc(path) 
#(Solo para windows. unidad de montaje + path)

os.path.walk(path, visit, arg) 
#Llama a la funcion y recorre con argumentos (arg, dirname, names) para todos los directorios donde path es la raiz.

os.path.supports_unicode_filenames 
#Verdadero si se pueden utilizar cadenas unicode en el nombre de los archivos.