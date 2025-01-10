"""
    Generador de cuadrados:
    Escribe un generador cuadrados(n) que devuelva los cuadrados de los números del 1 al n.
"""

def cuadrados(n):
    for i in range(1, n+1):
        yield f"{i} : {i**2}"

print("Cuadrados:")
for cuadrado in cuadrados(5):
    print(cuadrado)