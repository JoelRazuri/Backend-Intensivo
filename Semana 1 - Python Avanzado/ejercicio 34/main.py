"""
    Crea un paquete calculadora/ que contenga submódulos aritmetica.py y geometria.py.
    Define funciones como suma(), resta() en aritmetica.py y area_rectangulo() en geometria.py.
    Escribe un script main.py para importar y usar las funciones.
"""

from calculadora import aritmetica, geometria

print(aritmetica.suma(3,4))
print(aritmetica.resta(10,5))
print(geometria.area_rectangulo(2,15))