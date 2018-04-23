#Módulo para depurar dentro del código.
documentación:
https://docs.python.org/3.3/library/pdb.html
http://recursospython.com/guias-y-manuales/usando-el-depurador-pdb/

'''
Puede trabajar insertando puntos de detención en el código después de importar el módulo pdb 
pdb.set_trace()
O bien tras un fallo (posmortem) 

COMANDOS BÁSICOS:

help (comando)
Accede a lista de comandos o ayuda de comandos.

l, list(start, end)
Accede a las siguientes 11 lineas a cada ejecución (que se puede repetir apretando intro)
Con argumentos indicarango de lineas a mostrar.

w, where
Indica en que posición del programa nos encontramos.

q, quit
Cierra el depurador y el programa.

r, restart
Reinicia el programa

c, continue
Continúa el programa hasta el final.

n. next
Avanza a la siguiente linea del programa.

s, step
Avanza a la siguiente línea metiéndose en las funciones.

p, pp, print
Imprime el valor de una variable.

r, return.
Sale de la inspección de la función y vuelve al programa principal.

b, break (line)
Establece un punto de ruptura en la línea indicada. En este punto se detendrá
de nuevo el depurador si se ha introducio continue.
Si el comando está solo muestra una lista de los puntos de interrupción

disable (break), enable (break)
Habilita o inhabilita breaks

condition [n breakpoint] [condición]
ejecuta el breakpoint si se cumple una condición.
condition 1 anula la condicion.

clear n
Borra el break indicado o todos si no se especifica argumento.

unt, until (line)
Ejecuta el programa hasta la línea indicada.

j, jump (line)
Salta la ejecución hasta la línea indicada.



DEPURACIÓN POSMORTEM.

python -m pdb script.py
Correr script a traves del depurador:

pdb.pm()
En consola interactiva, inicia depuración que actúa sobre el último fallo.

Si queremos habilitar la depuración post-mortem en el manejo de una excepción, 
en su lugar usamos pdb.post_mortem().