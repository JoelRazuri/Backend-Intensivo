"""
    Simulación de una calculadora:
    Define una función crear_calculadora que acepte un número inicial y devuelva una función anidada con operaciones (sumar, restar, etc.).
"""

def crear_calculadora(num):
    def operaciones(operacion, valor):
        if operacion == "sumar":
            return num + valor
        elif operacion == "restar":
            return num - valor
        elif operacion == "multiplicar":
            return num * valor
        elif operacion == "dividir":
            if valor != 0:
                return int(num / valor)
            else:
                return "Error: división por cero"
        else:
            return "Operación no válida"
        
    return operaciones
    
calc = crear_calculadora(50)

print(calc("sumar", 5))
print(calc("restar", 40))
print(calc("multiplicar", 2))
print(calc("dividir", 10))
print(calc("dividir", 0))

# Alternativa si queres que el valor ingresado sea dinamico
# def crear_calculadora(num):
#     def operaciones(operacion, valor):
#         nonlocal num  # Permite modificar la variable num dentro de la función anidada
#         if operacion == "sumar":
#             num += valor
#         elif operacion == "restar":
#             num -= valor
#         elif operacion == "multiplicar":
#             num *= valor
#         elif operacion == "dividir":
#             if valor != 0:  
#                 num /= valor
#             else:
#                 return "Error: división por cero"
#         else:
#             return "Operación no válida"
#         return num

#     return operaciones

# # Crear calculadora
# calc = crear_calculadora(50)

# # Usar la calculadora
# print(calc("sumar", 5))        # 55
# print(calc("restar", 40))      # 15
# print(calc("multiplicar", 2))  # 30
# print(calc("dividir", 10))     # 3.0
# print(calc("dividir", 0))      # Error: división por cero.