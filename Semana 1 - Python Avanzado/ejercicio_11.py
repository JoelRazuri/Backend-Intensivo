"""
    Ejercicio de Función de Orden Superior:
    Crea una función aplicar_a_lista que reciba una lista de números y una función, y devuelva una nueva lista con el resultado de aplicar 
    la función a cada número de la lista.

    Pista: Usa map() o una función tradicional si prefieres no usar map().
"""

def aplicar_a_lista(func, lista):
    return func(lista)


def multiplicar_por_2(lista):
    return list(map(lambda x:x*2, lista))

print(aplicar_a_lista(multiplicar_por_2, [1,2,3]))


# Versión más simplificada
# def aplicar_a_lista(func, lista):
#     return [func(x) for x in lista]

# # Usando una función lambda directamente
# print(aplicar_a_lista(lambda x: x * 2, [1, 2, 3]))
