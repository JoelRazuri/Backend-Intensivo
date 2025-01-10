"""
    Crea una excepción personalizada NumeroNegativoError y úsala para lanzar un error si un número dado a una función es negativo.
"""
class NumeroNegativoError(Exception):
    def __init__(self, numero):
        super().__init__(f"Error: El número '{numero}' es negativo.")
        self.numero = numero


def verificar_numero_positivo(numero):
    if numero < 0:
        raise NumeroNegativoError(numero)
    return f"El número '{numero}' es positivo."

try:
    print(verificar_numero_positivo(10))  
    print(verificar_numero_positivo(-5))   
except NumeroNegativoError as e:
    print(e)
