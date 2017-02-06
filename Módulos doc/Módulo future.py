"""
 El modulo future ayuda a correr codigo Python 3.x bajo 2.7 sin usar
expresiones retorcidas.

La meta es permitir escribir hoy codigo 3.x limpio, moderno y compatible
hacia adelante y correrlo ademas con minimo esfuerzo tambien en 2.x

Está diseñado para ser usado de esta forma
    from __future__ import (division, absolute_import, print_function,
unicode_literals)
    from future import *

seguido por codigo limpio en python3 (con unas pocas restricciones) que
puede ser corrido sin cambios en python 2.7

En Python3 el from future import * no hace nada (ie no ensucia el
namespace); en python 2 tapa algunos builtins para proveer la semantica de
python 3

"""

Soporta en forma transparente el uso de modulos que han sido renombrados en
3, backport de algunas nuevas en 3, ...

El codigo se escribe en py3, y queda mucho mas limpio que usando six.

Incluye un script experimental futurize.py para ayudar a convertir tanto
codigo 2 como 3 a codigo compatible con ambas plataformas usando el modulo
future [2]

