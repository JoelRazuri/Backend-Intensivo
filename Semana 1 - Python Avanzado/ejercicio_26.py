"""
    Manejo de múltiples excepciones:
    Escribe un programa que tome una lista de números y un índice como entrada. Captura errores si el índice está fuera de rango 
    o si algún valor no es numérico.
"""

def funcion(lista_n, indice):
    try:
        return lista_n[indice] / 2
    except IndexError:
        return ("El índice esta fuera de rango")
    except TypeError:
        return ("Todos los datos tiene que ser númericos")

print(funcion([1, 'hola', 3, 4], 1))