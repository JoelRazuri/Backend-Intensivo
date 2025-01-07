"""
    Ejercicio con map():
    Tienes una lista de palabras. Usa map() para convertir todas las palabras en mayúsculas.
"""

lista_palabras = ['perro', 'gato', 'foca', 'elefante']

lista_palabras_mayus = map(lambda x: x.upper() , lista_palabras)

# lista_palabras_mayus = [x.upper() for x in lista_palabras]

print(list(lista_palabras_mayus))


# Solución alternativa para no tener que escribir la función lambda
# lista_palabras_mayus = list(map(str.upper, lista_palabras))
# print(lista_palabras_mayus)  # Resultado: ['PERRO', 'GATO', 'FOCA', 'ELEFANTE']