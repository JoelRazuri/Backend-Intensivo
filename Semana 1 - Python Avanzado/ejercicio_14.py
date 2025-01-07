"""
    Ejercicio con reduce():
    Dada una lista de números, utiliza reduce() para obtener el producto de todos los números de la lista.
"""

from functools import reduce


lista_numeros = [1, 2, 3, 4, 5, 6]

producto = reduce(lambda x,y: x*y, lista_numeros)

print(producto)