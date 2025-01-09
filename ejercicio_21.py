"""
    Combinar palabras: Dadas dos listas de palabras, ["rojo", "azul"] y ["coche", "moto"], crea una lista que contenga todas las combinaciones 
    posibles de una palabra de la primera lista con una de la segunda.
"""

colores = ["rojo", "azul"]

vehiculos = ["coche", "moto"]

combinaciones = [(x, y) for x in colores for y in vehiculos]

print(combinaciones)