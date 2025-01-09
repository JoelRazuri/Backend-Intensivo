"""
    Tablas de multiplicar: Crea una lista que contenga las tablas de multiplicar del 1 al 5.
"""

tablas = [[i * j for i in range(1,11)] for j in range(1,6)]

print(tablas)