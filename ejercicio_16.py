"""
    Lista de números pares: Crea una lista que contenga solo los números pares de una lista dada: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = [n for n in numeros if n % 2 ==0]

print(numeros_pares)