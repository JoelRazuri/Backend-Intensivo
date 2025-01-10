"""
    Captura de errores:
    Escribe una función que divida dos números. Captura la excepción si el denominador es cero e imprime un mensaje de error adecuado.
"""

def division(numero1, numero2):
    try:
        return numero1 // numero2 
    except ZeroDivisionError as e:
        return f"Error: {e}"
    

print(division(10,2))
print(division(15,3))
print(division(20,0))