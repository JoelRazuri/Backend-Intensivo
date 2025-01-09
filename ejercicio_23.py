"""
    Contador de instancias: Crea una clase Animal con un atributo de clase que lleve el conteo de cuántos animales han sido creados. 
    Usa un método de clase para devolver el número de instancias.
"""

class Animal():
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Animal.incrementar()


    @classmethod
    def incrementar(cls):
        cls.contador+=1
        return cls.contador
    
    @classmethod
    def obtener_contador(cls):
        return cls.contador
    

perro = Animal("Dibu")
gato = Animal("Garfield")

print(Animal.obtener_contador())
    

