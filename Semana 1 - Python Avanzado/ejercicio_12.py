"""
    Ejercicio con Lambda:
    Crea una lista de números y usa una función lambda para encontrar los números que son múltiplos de 3.

    Pista: Usa filter() y una expresión lambda.
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

multiplos_de_3 = filter(lambda x: x%3 == 0, lista)

print(list(multiplos_de_3))


# Usando list comprehension como alternativa
# multiplos_de_3_alt = [x for x in lista if x % 3 == 0]
# print(multiplos_de_3_alt)  # Resultado: [3, 6, 9, 12]