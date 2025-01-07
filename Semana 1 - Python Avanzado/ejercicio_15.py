"""
    Ejercicio práctico - Combine todo:
    Crea una función procesar_lista que reciba una lista de números, los multiplique por 2 usando map(), elimine los números impares usando filter(),
    y luego sume todos los números restantes usando reduce().
"""
from functools import reduce

def procesar_lista(lista):
    if not all(isinstance(x, (int,float)) for x in lista):
        return "La lista solo puede contener números"
    
    lista = list(map(lambda x: x*2, lista))
    lista = list(filter(lambda x: x%2 == 0, lista))

    suma = reduce(lambda x,y: x + y, lista, 0)  # Usar 0 como valor inicial para listas vacías

    return suma

print(procesar_lista([1,2,3,4]))
print(procesar_lista([1,2,3,'hola']))
print(procesar_lista([]))

# Función documentada y con nombres distintos de variables para no generar confuciones
# def procesar_lista(lista):
#     # Validar que todos los elementos sean números
#     if not all(isinstance(x, (int, float)) for x in lista):
#         return "La lista solo puede contener números"
    
#     # Multiplicar cada número por 2
#     multiplicados = map(lambda x: x * 2, lista)
    
#     # Filtrar números pares
#     pares = filter(lambda x: x % 2 == 0, multiplicados)
    
#     # Sumar todos los números restantes
#     suma = reduce(lambda x, y: x + y, pares, 0)  # Usar 0 como valor inicial para listas vacías
    
#     return suma

# # Pruebas
# print(procesar_lista([1, 2, 3, 4]))  # Resultado esperado: 12
# print(procesar_lista([1, 2, 3, 'hola']))  # Resultado esperado: "La lista solo puede contener números"
# print(procesar_lista([]))  # Resultado esperado: 0