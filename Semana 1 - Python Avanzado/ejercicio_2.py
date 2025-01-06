"""
    Escribe una función multiplicar que acepte una lista o tupla de números y devuelva el producto de todos ellos. 
    Asegúrate de manejar el desempaquetado correctamente.
"""

def multiplicar(*args):
    resultado = 1

    for num in args:
        resultado = resultado * num
    
    return resultado

print(multiplicar(2,3))
print(multiplicar(2,3,5))
print(multiplicar(2,3,6))


# Solución más avanzada y Pythonic

# from functools import reduce
# from operator import mul
# from typing import Union

# def multiplicar(*args: Union[int, float]) -> Union[int, float]: #se asegura que los argumentos que se pasen sean de tipo entero o flotante
#     if not args:  # Si no se pasan argumentos, devolvemos 1 explícitamente
#         return 1
#     return reduce(mul, args)