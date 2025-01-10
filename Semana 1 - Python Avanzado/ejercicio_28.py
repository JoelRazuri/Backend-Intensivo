"""
    Secuencia de números:
    Crea un generador generar_numeros(n) que devuelva números desde 1 hasta n.
"""

def generador_numeros(n):
    for i in range(1,n+1):
        yield i


for numeros in generador_numeros(5):
    print(numeros)