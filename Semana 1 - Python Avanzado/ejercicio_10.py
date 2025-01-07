"""
    Closure para un contador:
    Escribe una función crear_contador que devuelva una función anidada. Cada vez que se llame a la función anidada, debe incrementar y devolver el 
    contador.
"""

def crear_contador(i=0):
    def incrementar():
        nonlocal i
        i+=1
        return i

    return incrementar

contador1 = crear_contador()
contador2 = crear_contador(10)

print(contador1())
print(contador1())
print(contador1())

print(contador2())
print(contador2())
print(contador2())