"""
    Funciones anidadas simples: Crea una función crear_saludo que acepte un idioma como argumento y devuelva una función anidada que reciba un nombre 
    y devuelva un saludo en el idioma indicado.

    Por ejemplo, si el idioma es "es", devuelve "Hola, <nombre>!".
"""

def crear_saludo(idioma):
    def saludo(nombre):
        return f"{idioma}, {nombre}!"

    return saludo

saludo_espaniol = crear_saludo("Hola")
saludo_ingles = crear_saludo("Hello")

print(saludo_espaniol("Joel"))
print(saludo_ingles("Joe"))