"""
    Escribe una función crear_lista que acepte un número variable de argumentos y los almacene en una lista. 
    Además, debe aceptar un argumento opcional inicial que, si se pasa, se agregue al principio de la lista.
"""

def crear_lista(*args, inicial=None):
    lista = []

    if inicial is not None:
        lista.append(inicial)

    for i in args:
        lista.append(i)
    
    return lista


# Mejorando el códgio
# def crear_lista(*args, inicial=None):
#     lista = [inicial] if inicial is not None else []
#     lista.extend(args)
#     return lista


print("Lista 1:")
print(crear_lista(1,2,3,5,"Joel",inicial="Pedro"))

print("------------")

print("Lista 2:")
print(crear_lista(16,2,33,5,"Joel"))


