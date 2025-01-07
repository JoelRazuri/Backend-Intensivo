"""
    Escribe una función combinar_listas que acepte dos listas y las combine alternando sus elementos. 
    Por ejemplo, con las listas [1, 2, 3] y ['a', 'b', 'c'], el resultado sería [1, 'a', 2, 'b', 3, 'c'].

    Pista avanzada:
        Considera usar zip() para combinar iterables de forma pareja.
"""

def combinar_listas(lista1, lista2):
    if not lista1 and not lista2:
        return "Ambas listas están vacías."
    elif not lista1:
        return f"La lista 1 está vacía. Lista 2: {lista2}"
    elif not lista2:
        return f"La lista 2 está vacía. Lista 1: {lista1}"
    
    lista_combinada = [item for pair in zip(lista1, lista2) for item in pair]

    if len(lista1) > len(lista2):
        lista_combinada.extend(lista1[len(lista2):])
    elif len(lista2) > len(lista1):
        lista_combinada.extend(lista2[len(lista1):])

    return lista_combinada


print(combinar_listas([],[]))
print(combinar_listas([1,2,3],[]))
print(combinar_listas([],["a","b","c"]))
print(combinar_listas([1,2,3],["a","b","c","d","e"]))