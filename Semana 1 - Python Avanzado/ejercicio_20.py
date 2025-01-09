""""
    Números en matrices: Dada una lista de listas, como [[1, 2], [3, 4], [5, 6]], crea una lista con todos los números planos (sin anidación).
"""

lista = [[1, 2], [3, 4], [5, 6]]

lista_planos = [numero for sublista in lista for numero in sublista]

print(lista_planos)