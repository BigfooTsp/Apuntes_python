 ''' Facilita el uso de argumentos
 El módulo argparse (PEP389) módulo de análisis de línea de comandos que ofrece más funcionalidad 
 que los módulos de análisis de línea de comandos existentes en la biblioteca estándar.

A partir de la versión Python 2.7 y 3.2 el módulo argparse sustituye al módulo optparse.

Para usarlo, se crea un objeto (ArgumentParser) al que se le añaden argumentos mediante la 
función add_argument(). Despues, se indica mediante parse_args() que analice los argumentos
introducidos por el intérprete y que los añada como propiedades del objeto'''

# -*- coding: cp1252 -*-
from argparse import ArgumentParser
 
# ArgumentParser con una descripción de la aplicación 
# (https://docs.python.org/2/library/argparse.html#argumentparser-objects)
parser = ArgumentParser(description='%(prog)s is an ArgumentParser demo')
 
# Argumento posicional. Los argumentos posicionales son obligatorios.
parser.add_argument('arg1')
 
# Un argumento posicional con una descripción 
parser.add_argument('arg2', help='help for arg2')
 
# Un argumento posicional con un tipo definido de tipo int 
# (https://docs.python.org/2/library/argparse.html#type)
parser.add_argument('arg3', help='help for arg3', type=int)
 
# Argumento posicional con tres opciones posibles 
# (https://docs.python.org/2/library/argparse.html#choices)
parser.add_argument('arg4', choices=['rock', 'paper', 'scissors'])
 
# Argumento opcional. Si se pametriza, requiere acompañarlo de un valor
parser.add_argument('-opt1')
 
# Un argumento opcional puede tener varios nombres
parser.add_argument('-opt2', '--option2')
 
# Argumento opcional con una descripción. Si se pametriza, requiere 
# acompañarlo de un valor de tipo int
parser.add_argument('-opt3', help='help for opt3', type=int)
 
# Argumento opcional con una descripción. Si se pametriza, requiere 
# acompañarlo de un valor de tipo int. Por defecto el valor es 10
parser.add_argument('-opt4', help='help for opt4', type=int, default=10)
 
# Argumento opcional. Con 'action' damos valor si el argumento se parametriza 
# (https://docs.python.org/2/library/argparse.html#action)
parser.add_argument('-opt5', '--option5', help='help for opt5', 
action='store_true', default=False)
 
# Argumento opcional requerido
parser.add_argument('-opt6', required=True)
 
# Argumento opcional con tres opciones posibles
# (https://docs.python.org/2/library/argparse.html#choices)
parser.add_argument('-opt7', choices=['rock', 'paper', 'scissors'])
 
# Argumento opcional que requiere dos argumentos
parser.add_argument('-opt8', nargs=2)
 
# Argumento opcional que requiere de 1 a N argumentos
parser.add_argument('-opt9', nargs='+')
 
# Argumento opcional que requiere de 0 a N argumentos
parser.add_argument('-opt10', nargs='*')

# dest indica el nombre que se dará a la variable de destino.
parser.add_argument('opt11', dest='path')

 
# Por último indicar que analice los argumentos. Devolverá cada argumento indicado en 
# línea de comandos como propiedades del objeto generado.
args = parser.parse_args()
 
# Imprimir los parametros
print 'args.arg1:', args.arg1
print 'args.arg2:', args.arg2
print 'args.arg3:', args.arg3
print 'args.arg2:', args.arg4
print 'args.opt1:', args.opt1
print 'args.opt2:', args.option2
print 'args.opt3:', args.opt3
print 'args.opt4:', args.opt4
print 'args.opt5:', args.option5
print 'args.opt6:', args.opt6
print 'args.opt7:', args.opt7
print 'args.opt8:', args.opt8
print 'args.opt9:', args.opt9
print 'args.opt10:', args.opt10
print 'args.opt11:', args.opt10


''' 
# Ayuda básica

  >python argcons.py
  usage: argcons.py [-h] [-opt1 OPT1] [-opt2 OPTION2] [-opt3 OPT3] [-opt4 OPT4]
                    [-opt5] -opt6 OPT6 [-opt7 {rock,paper,scissors}]
                    [-opt8 OPT8 OPT8] [-opt9 OPT9 [OPT9 ...]]
                    [-opt10 [OPT10 [OPT10 ...]]]
                    arg1 arg2 arg3 {rock,paper,scissors}
  argcons.py: error: too few arguments


# Mostrar ayuda extendida

  >python argcons.py -h
  usage: argcons.py [-h] [-opt1 OPT1] [-opt2 OPTION2] [-opt3 OPT3] [-opt4 OPT4]
                    [-opt5] -opt6 OPT6 [-opt7 {rock,paper,scissors}]
                    [-opt8 OPT8 OPT8] [-opt9 OPT9 [OPT9 ...]]
                    [-opt10 [OPT10 [OPT10 ...]]]
                    arg1 arg2 arg3 {rock,paper,scissors}

  argcons.py is an ArgumentParser demo

  positional arguments:
    arg1
    arg2                  help for arg2
    arg3                  help for arg3
    {rock,paper,scissors}

  optional arguments:
    -h, --help            show this help message and exit
    -opt1 OPT1
    -opt2 OPTION2, --option2 OPTION2
    -opt3 OPT3            help for opt3
    -opt4 OPT4            help for opt4
    -opt5, --option5      help for opt5
    -opt6 OPT6
    -opt7 {rock,paper,scissors}
    -opt8 OPT8 OPT8
    -opt9 OPT9 [OPT9 ...]
    -opt10 [OPT10 [OPT10 ...]]

# Ejemplo de uso

  Shell

  >python argcons.py  a b 15 rock -opt6 c -opt7 rock -opt8 1 2 -opt9 1 2 3 d e f -opt10
  args.arg1: a
  args.arg2: b
  args.arg3: 15
  args.arg2: rock
  args.opt1: None
  args.opt2: None
  args.opt3: None
  args.opt4: 10
  args.opt5: False
  args.opt6: c
  args.opt7: rock
  args.opt8: ['1', '2']
  args.opt9: ['1', '2', '3', 'd', 'e', 'f']
  args.opt10: []
'''

# el parámetro 'action' indica la acción a realizar, pudiendo ser:
'''
store: almacena el valor (acción predeterminada)
store_const: si el argumento es pasado, almacenará el valor definido en el parámetro
            const (ver más abajo). Es útil cuando se requiere recibir un flag pero sin valor asociado
store_true / store_false: Igual que store_const pero no necesita definir el valor de const
            ya que almacenarán True o False respectivamente en caso que el argumento sea pasado
append:  almacena los valores del argumento en una lista. Es útil cuando un mismo argumento puede 
        indicarse varias veces con diferentes valores ej: (argumento = ['valor1', 'valor2'])
append_const: almacena el valor de const en una lista. Especialmente útil cuando
            el valor de diferentes argumentos es una constante y se los necesita
            de forma unificada. Requiere que
            el parámetro dest (ver más abajo) posea el mismo valor en los diferentes argumentos.''''

argp.add_argument('--table', action='store')
# --table foo genera: table = 'foo'
argp.add_argument('--table', action='store_const', const='users')
# --table genera: table = 'users'
argp.add_argument('--table', action='append')
# --table foo --table bar genera: table = ['foo', 'bar']
argp.add_argument('--php', dest='lenguajes', action='append_const', const='php')
argp.add_argument('--python', dest='lenguajes',action='append_const', const='python')
# --php --python genera: lenguajes = ['php', 'python']
