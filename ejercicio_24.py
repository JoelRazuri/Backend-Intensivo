"""
    Rectángulo: Crea una clase Rectangulo con atributos base y altura. Usa una propiedad llamada area para calcular el área del rectángulo sin 
    definir un método explícito.
"""

class Rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property
    def area(self):
        return self.base * self.altura
    

rectangulo = Rectangulo(2,5)

print(rectangulo.area)
