''' EJECUTAR COMANDOS EXTERNOS CON PYTHON:

http://python-para-impacientes.blogspot.com.es/2014/02/ejecutar-un-comando-externo.html
'''
#!usr/bin/env Python
# -*- coding: utf-8 -*-
 
import os, sys
import subprocess
 
# Ejecutar un comando con "os.system(comando)" y mostrar en
# pantalla la salida del comando y el resultado de la 
# ejecución.
# Si su valor es 0 la ejecución finalizó con éxito.
 
valor1 = os.system("whoami")
print("Resultado:", valor1)
 
 
# Ejecutar un comando "erróneo" con "os.system(comando)"
 
valor2 = os.system("whoamix")
print("Resultado:", valor2)
 
 
# Ejecutar varios comandos con "os.system(comando)"
 
comando3 = "ls -l | grep 'txt' >textos.txt"
valor3 = os.system(comando3)
print("Resultado:", valor3)
 
 
# Ejecutar un comando con "os.popen(comando)" y capturar su 
# salida
 
comando4 = "uname -srmo"
salida4 = os.popen(comando4).read()
print("Salida:\n", salida4)
 
 
# A continuación, se muestran varios ejemplos con el módulo 
# "subprocess" que genera un nuevo proceso para ejecutar el
# comando permitiendo controlar su ejecución y obtener su 
# salida y/o errores que pudieran darse.
 
# Ejecutar un comando externo con "subprocess.call", mostrar 
# su salida y el resultado de su ejecución.
 
valor5 = subprocess.call(["ping", "-c 6", "www.elpais.es"])
print("Este texto se mostrará después de ejecutar el comando")
print("Resultado:", valor5)
 
 
# Ejecutar un comando externo en paralelo con 
# "subprocess.Popen" con wait() se espera a que termine
# la ejecución del subproceso
# Todas las líneas de código delante de wait() se 
# ejecutarán en paralelo a la ejecución del comando.
# También, se mostrará si la ejecución terminó o no
# con éxito
 
proceso6 = subprocess.Popen(['ls', '-lha'])
for num in range(100):
    print ("Este texto se mostrará antes")
 
valor6 = proceso6.wait()
print ("Este texto se mostrará después")
print ("Resultado:", valor6)
 
 
# Ejecutar un comando externo en paralelo con
# "subprocess.Popen"
 
proceso7 = subprocess.Popen(['ls', '-lha'])
for num in range(300):
    print ("Este texto se mostrará en paralelo")
 
# Ejecutar un comando en paralelo con 
# "subprocess.Popen" y capturar su salida y
# los errores que puedieran darse
 
proceso8 = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
errores8 = proceso8.stderr.read()
salida8 = proceso8.stdout.read()
proceso8.stderr.close()
proceso8.stdout.close()
print("Salida de errores:\n")
errores8 = errores8.decode(sys.getdefaultencoding())
print(errores8)
salida8 = salida8.decode(sys.getdefaultencoding())
print("Salida del comando:\n")
print(salida8)
 
 
# Ejecutar un comando externo con "subprocess.Popen" y 
# obtener su salida y los errores que puedan darse (Otra 
# manera de hacerlo)
# En el ejemplo se provoca un error y se muestra el texto
# de su salida
 
proceso9 = subprocess.Popen(["ping", "-zz 4", "www.elpais.es"], stdout=subprocess.PIPE)
salida9, errores9 = proceso9.communicate()
print(salida9.decode(sys.getdefaultencoding()))
if errores9 != None:
    print(errores9.decode(sys.getdefaultencoding()))
 
 
# Para resolver variables de entorno, patrones globales y
# otras caracteristicas de la shell hay que incluir el 
# parámetro "shell = True"
 
print("Correcto  : subprocess.call('echo $HOME', shell=True)")
print("Incorrecto: subprocess.call('echo $HOME')") # Es equivalente a shell = False
subprocess.call('echo $HOME', shell=True)
 
 
# Ejecutar un comando externo con subprocess.Popen() y
# obtener su salida en tiempo real
 
comando11 = "ping -c3 www.elpais.es"
resultado11 = subprocess.Popen(comando11, shell=True, stdout=subprocess.PIPE)
for salida11 in resultado11.stdout:
 print(salida11.decode(sys.getdefaultencoding()).rstrip())
  
 
# Ejecutar un comando externo con subprocess.Popen()
# y obtener la salida en tiempo real (Otra forma de
# hacerlo)
 
comando12 = "ping -c2 www.elpais.es"
resultado12 = subprocess.Popen(comando12, shell=True, stdout=subprocess.PIPE)
while resultado12.poll() is None:
    salida12 = resultado12.stdout.readline()
    print(salida12.decode(sys.getdefaultencoding()).rstrip())