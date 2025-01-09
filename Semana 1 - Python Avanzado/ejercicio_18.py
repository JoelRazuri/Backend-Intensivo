"""
    Números mayores que 5 al cuadrado: Dada una lista de números [1, 3, 5, 7, 9, 11], crea una nueva lista con los cuadrados de los números 
    que son mayores que 5.
"""

numeros = [1, 3, 5, 7, 9, 11]

mayores_que_5 = [n**2 for n in numeros if n > 5]

print(mayores_que_5)