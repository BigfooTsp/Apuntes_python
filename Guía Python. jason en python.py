'''

JSON (JavaScript Object Notation)
http://programacion.net/articulo/como_trabajar_con_datos_json_utilizando_python_1403

### Módulo json ###


'''

import json


# loads()
def loads():
	jsonData = '{"name": "Frank", "age": 39}'
	jsonToPython = json.loads(jsonData)

	print (jsonToPython)
#{'age': 39, 'name': 'Frank'}

# dumps()
def dumps():
	pythonDictionary = {'name':'Bob', 'age':44, 'isEmployed':True}
	dictionaryToJson = json.dumps(pythonDictionary)

'''
Jason solo permite objetos de tipo 
Lists, Dictionaries, Booleanas, Numbers, Character Strings y None
cualquier otro tipo necesitará ser convertidos a alguno de los mencionados

Tambien se puede hacer lo siguiente:
'''
class Employee(object):
    def __init__(self, name):
        self.name = name

abder = Employee('Abder')

# si lo intentamos conbertir tal cual:
'''
abder = json.dumps(Employee)

>    raise TypeError(repr(o) + " is not JSON serializable")
TypeError: <class '__main__.Employee'> is not JSON serializable
'''

def jsonDefault(object):
    return object.__dict__

jsonAbder = json.dumps(abder, default=jsonDefault)

print (jsonAbder)
# {"name": "Abder"}