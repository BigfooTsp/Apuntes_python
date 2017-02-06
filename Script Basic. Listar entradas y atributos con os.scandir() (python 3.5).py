'''
Script que utiliza la librería 'os' y 'time' para leer los archivos del directorio del script
obteniendo de cada archivo su tamnañpo, fecha, útlimo acceso y última modificación.
Al final, el número total de archivos y el tamaño total.

http://python-para-impacientes.blogspot.com.es/2015/09/explorando-directorios-con-listdir-walk.html

Aquí se utiliza os.scandir() DISPONIBLE DESDE PYTHON 3.5 '''

# script:

import os
from datetime import datetime
 
ruta_app = os.getcwd() 
contenido = os.listdir(ruta_app)
total = 0
archivos = 0
formato = '%d-%m-%y %H:%M:%S'
linea = '-' * 40
 
contenido = os.scandir(ruta_app)
for elemento in contenido:
    if not os.access(elemento.path, os.X_OK) and elemento.is_file():
        archivos += 1
        estado = elemento.stat()        
        tamaño = estado.st_size
        ult_acceso = datetime.fromtimestamp(estado.st_atime)
        modificado = datetime.fromtimestamp(estado.st_mtime)
        ult_acceso = ult_acceso.strftime(formato)
        modificado = modificado.strftime(formato)
        total += tamaño
        print(linea)
        print('archivo      :', elemento.name)
        print('permisos     :', estado.st_mode)
        print('modificado   :', modificado)        
        print('último acceso:', ult_acceso)
        print('tamaño (Kb)  :', round(tamaño/1024, 1))
 
print(linea)
print('Núm. archivos:', archivos)
print('Total (kb)   :', round(total/1024, 1))