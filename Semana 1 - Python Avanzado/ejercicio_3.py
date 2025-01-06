"""
    Escribe una función filtrar_pares que acepte una lista de números y devuelva una nueva lista con solo los números pares.
    
    Pista avanzada:
        Considera usar listas por comprensión o la función filter de Python.
"""

def filtrar_pares(*args):
    lista_pares = [x for x in args if x % 2 == 0]
    
    return lista_pares

print(filtrar_pares(1,2,3,4,5,6))


# Otra solución usando filter y lambda
# def filtrar_pares(*args):
#     return list(filter(lambda x: x % 2 == 0, args))  

# print(filtrar_pares(1, 2, 3, 4, 5, 6))