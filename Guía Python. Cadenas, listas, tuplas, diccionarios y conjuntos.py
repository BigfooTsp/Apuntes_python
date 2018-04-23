# OPERACIONES CON CADENAS:

	cadena1 = 'tengo una yama que Yama se llama'  # declara variable
	lista1 = ['pera', 'manzana', 'naranja', 'uva']  # declara lista
	longitud = len(cadena1)  # 32, devuelve longitud de la cadena
	elem = len(lista1)  # 4, devuelve nº elementos de la lista 
	cuenta = cadena1.count('yama')  # 1, cuenta apariciones de la palabra 'yama'
	print(cadena1.find('yama'))  # 10, devuelve posición del elemento buscado 
	cadena2 = cadena1.join('***')  # inserta cadena1 entre caracteres  
	lista1 = cadena1.split(' ')  # divide cadena por separador → lista
	tupla1 = cadena1.partition(' ')  # divide cadena por separador → tupla 
	cadena2 = cadena1.replace('yama','cabra',1)  # busca y sustituye términos 
	numero = 3.14  # asigna número con decimales
	cadena3 = str(numero)  # convierte número a cadena
	if cadena1.startswith("tengo"):  # evalúa si cadena1 comienza por “tengo”: True
	if cadena1.endswith("llama"):  # evalúa si cadena1 termina por “llama”: True
	if cadena1.find("llama") != -1:  # evalúa si cadena1 contiene la palabra “llama”
	cadena4 = 'Python'  # asigna una cadena a una variable
	print(cadena4[0:4])  # muestra desde la posición 0 a 4: "Pyth"
	print(cadena4[1])  # muestra la posición 1: "y"
	print(cadena4[:3] + '-' + cadena4[3:])  # muestra "Pyt-hon"
	print(cadena4[:-3])  # muestra todo menos las tres últimas: "Pyt"
	 
	cadena5 = "  abc;123  "   # declara una variable con una cadena alfanumérica
	print(cadena5.rstrip())   # suprime caracteres en blanco (y \t\n\r) por la derecha: "  abc;123"
	print(cadena5.lstrip())   # suprime caracteres en blanco (y \t\n\r) por la izquierda: "abc;123  "
	print(cadena5.strip())   # suprime caracteres en blanco (y \t\n\r) por la derecha e izquierda: "abc;123"
	print(cadena5.strip("123456790; "))  # suprime caracteres del argumento por la derecha e izquierda: "abc"
	cadena6 = "Mar"   # declara una variable
	print(cadena5.upper())   # convierte la cadena a mayúsculas: "MAR"
	print(cadena5.lower())   # convierte la cadena a minúsculas: "mar"

# OPERACIONES CON LISTAS Y TUPLAS:

	lista1 = ['uno', 2, True]  # declara una lista heterogénea
	lista2 = [1, 2, 3, 4, 5]  # declara lista numérica (homogénea)
	lista3 = ['nombre', ['calle', 'ciudad']]  # declara una lista dentro de otra
	lista4 = [54,45,44,22,0,2,99]  # declara una lista numérica
	print(lista1)  # ['uno', 2, True], muestra toda la lista
	print(lista1[0])  # uno, muestra el primer elemento de la lista
	print(lista2[-1])  # 5, muestra el último elemento de la lista
	print(lista3[1][0])  # calle, primer elemento de la lista anidada
	print(lista2[0:3:1])  # [1, 2, 3], responde al patrón inicio:fin:paso
	print(lista2[::-1])  # devuelve la lista ordenada al revés
	lista1[2] = False  # cambia el valor de un elemento de la lista
	lista2[-2] = lista2[-2] + 1  # 4 + 1 → 5 – cambia el valor de un elemento
	lista2.pop(0)  # borra elemento indicado o último si no indica
	lista1.remove('uno')  # borra el primer elemento que coincida
	del lista2[1]  # borra el segundo elemento (por índice)  
	lista2 = lista2 + [6]  # añadiendo un elemento al final de la lista
	lista2.append(7)  # añade un elemento al final con append()
	lista2.extend([8, 9])  # extiende la lista con otra lista por el final
	lista1.insert(1, 'dos')  # inserta nuevo elemento en una posición
	del lista2[0:3]  # borra los elementos desde:hasta
	lista2[:] = []  # borra todos los elementos de la lista 
	print(lista1.count(2))  # cuenta el nº de veces que aparece 2
	print(lista1.index("dos"))  # busca la posición que ocupa un elemento
	lista3.sort()  # ordena la lista
	lista3.sort(reverse=True)  # ordena la lista en orden inverso
	lista5 = sorted(lista4)  # ordena lista destino 
	tupla1 = (1, 2, 3)  # declara una tupla (se usan paréntesis)...
	tupla2 = 1, 2, 3  # ...aunque pueden declararse sin paréntesis
	tupla3 = (100,)  # con un solo un elemento hay que poner “,”
	tupla4 = tupla1, 4, 5, 6  # anida tuplas
	tupla5 = ()  # declara una tupla vacía
	tupla2[0:3]  # (1, 2, 3), accede a los valores desde:hasta

# DICCIONARIOS O APLICACIONES ASOCIATIVAS:
 
	capitales = {'Chile':'Santiago',
	              'España':'Madrid',
	              'Francia':'París'}  # declara el diccionario
	               
	print('La capital de Chile es', capitales['Chile'])  # muestra 'Santiago'
	del capitales['Francia']  # borra el par Francia:París
	print('\nHay {0} países\n'.format(len(capitales)))  # 'Hay 2 países'
	for pais, capital in capitales.items():  # recorre diccionario
	 print('Capital de {0} : {1}'.format(pais, capital))  # muestra todos los pares
	 
	capitales['Portugal'] = 'Lisboa'  # agrega par Portugal:Lisboa
	if 'Portugal' in capitales:  # recorre diccionario
 print('\nCapital de Portugal:', capitales['Portugal']) # 'Lisboa'

# OPERACIONES CON DICCIONARIOS:

	dic1 = { 'Lorca' : 'Escritor', 'Goya' : 'Pintor'}  # declara diccionario 
	print(dic1)  # {'Goya': 'Pintor', 'Lorca': 'Escritor'}
	dic2 = dict((('mesa', 5), ('silla', 10)))  # declara a partir de una tupla
	dic3 = dict(ALM=5, CAD=10)  # declara a partir de cadenas simples 
	dic4 = dict([(z, z**2) for z in (1, 2, 3)])  # declara a partir de patrón
	print(dic4)  # muestra {1: 1, 2: 4, 3: 9}
	print(dic1['Lorca'])  # escritor, acceso a un valor por clave
	print(dic1.get('Gala', 'no existe'))  # acceso a un valor por clave
	if 'Lorca' in dic1: print('está')  # comprueba si existe una clave
	print(dic1.items())  # obtiene una lista de tuplas clave:valor
	print(dic1.keys())  # obtiene una lista de las claves
	print(dic1.values())  # obtiene una lista de los valores
	dic1['Lorca'] = 'Poeta'  # añade un nuevo par clave:valor
	dic1['Amenabar'] = 'Cineasta'  # añade un nuevo par clave:valor
	dic1.update({'Carreras' : 'Tenor'})  # añadir con update()
	del dic1['Amenábar']  # borra un par clave:valor 
	print(dic1.pop('Amenabar', 'no está'))  # borra un par clave:valor

# RECORRER SECUENCIAS Y DICCIONARIOS:
	artistas = { 'Lorca' : 'Escritor', 'Goya' : 'Pintor'}  # declara diccionario 
	paises = ['Chile','España','Francia','Portugal']  # declara lista países
	capitales = ['Santiago','Madrid','París','Lisboa']  # declara lista capitales
	for c, v in artistas.items(): print(c,':',v)  # recorre diccionario artistas
	for i, c in enumerate(paises): print(i,':',c)  # recorre lista países 
	for p, c in zip(paises, capitales): print(c,' - ',p)  # recorre ¡ las 2 listas !
	for p in reversed(paises): print(p,)  # recorre en orden inverso
	for c in sorted(paises): print(c,)  # recorre secuencia ordenada

	for num in range(7): print(num)  # recorre del 0 al 6
	for num in range(1,8): print(num)  # recorre del 1 al 7
	for num in range(10,50,5): print(num)  # recorre del 10 al 45 de 5 en 5
	for num in range(0,-10,-1): print(num)  # recorre del 0 al -9 de -1 en -1
	lista = ["Chorizo","Jamón","Morcilla","Salchichón"]  # declara lista
	for elemento in range(len(lista)):  # recorre los elementos de la lista
	    print (elemento, lista[elemento])  # muestra posición y elemento

	cadena = 'Python'  # asigna cadena a variable
	lista = [1, 2, 3, 4, 5]  # declara lista
	if 'y' in cadena: print('“y” está en “Python”')  # uso de in (contiene)
	if 6 not in lista: print('6 no está en la lista')  # uso de not in (no contiene)
	if 'abcabc'  is 'abc' * 2: print('Son iguales')  # uso de is (es igual a)

# OPERACIONES CON CONJUNTOS:
	lista = ['vino', 'cerveza', 'agua', 'vino']  # define lista
	bebidas = set(lista)  # define conjunto a partir de una lista
	print('vino' in bebidas)  # True, 'vino' está en el conjunto
	print('anis' in bebidas)  # False, 'anis' no está en el conjunto
	print(bebidas)  # imprime {'agua', 'cerveza', 'vino'}
	bebidas2 = bebidas.copy()  # crea nuevo conjunto a partir de copia
	print(bebidas2)  # imprime {'agua', 'cerveza', 'vino'}
	bebidas2.add('anis')  # añade un nuevo elemento 
	print(bebidas2.issuperset(bebidas))  # True, bebidas es un subconjunto
	bebidas.remove('agua')  # borra elemento
	print(bebidas & bebidas2)  # imprime elementos comunes
	tapas = ['croquetas', 'solomillo', 'croquetas']  # define lista
	conjunto = set(tapas)  # crea conjunto (sólo una de croquetas)
	if 'croquetas' in conjunto:  # evalúa si croquetas está en conjunto
	conjunto1 = set('Python')  # define conjunto: P, y, t, h, o, n 
	conjunto2 = set('Pitonisa')  # define conjunto: P, i, t, o, n, s, a
	print(conjunto2 - conjunto1)  # aplica diferencia: s, i, a
	print(conjunto1 | conjunto2)  # aplica unión: P, y, t, h, o, n, i, s, a 
	print(conjunto1 & conjunto2)  # aplica intersección: P, t, o, n
	print(conjunto1 ^ conjunto2)  # aplica diferencia simétrica: y, h, i, s, a