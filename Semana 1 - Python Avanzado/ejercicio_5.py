"""
    Diseña una función reversa_palabras que tome una lista de palabras y devuelva una nueva lista con las palabras en orden inverso.

    Pista avanzada:
        Las rebanadas (slicing) de listas ([::-1]) son una forma compacta de invertir listas o cadenas.
"""


def reversa_palabras(lista):
    if not lista:
        return "La lista está vacía."
    
    nueva_lista = lista[::-1]

    return nueva_lista


print(reversa_palabras(["Joel", "pelota", "basura"]))


# Versión si queres invertir las palabras dentro de la lista
def reversa_palabras_2(lista):
    if not lista:
        return "La lista está vacía."
    
    nueva_lista = [x[::-1] for x in lista]

    return nueva_lista


print(reversa_palabras_2(["Joel", "pelota", "basura"]))


# Versión si queres invetir la lista y también invertir las palabras dentro de la lista
def reversa_palabras_3(lista):
    if not lista:
        return "La lista está vacía."
    
    nueva_lista = [x[::-1] for x in lista[::-1]]

    return nueva_lista


print(reversa_palabras_3(["Joel", "pelota", "basura"]))