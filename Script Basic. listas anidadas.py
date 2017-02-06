# imprimir todos los elementos de un objeto con varias listas anidadas


lista_anidada = [1, [2, [3, 4, [5, 6], 7]], 8, [9, 10]]


def imprimir(lista):
    for elemento in lista:
        if isinstance(elemento, list):
            imprimir(elemento)
        else:
            print(elemento)


imprimir(lista_anidada)

'''
>>> 
1
2
3
4
5
6
7
8
9
10
'''