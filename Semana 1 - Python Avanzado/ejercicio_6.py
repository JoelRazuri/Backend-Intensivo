"""
    Escribe una función sumar_elementos que reciba una lista de números y devuelva la suma de todos ellos.

    Pista avanzada:
        La función sum() es ideal para sumar elementos de un iterable.
"""

def sumar_elementos(lista):
    if not all(isinstance(x, (int, float)) for x in lista):
        return "Error: La lista debe contener solo números."
    
    suma = sum(lista)

    return suma

print(sumar_elementos([1,4,2]))
print(sumar_elementos([1,"hola",2]))