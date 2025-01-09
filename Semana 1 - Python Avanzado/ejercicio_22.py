"""
    Convertidor de temperatura: Crea una clase Temperatura que tenga un método estático llamado celsius_a_fahrenheit para convertir grados Celsius a 
    Fahrenheit.
"""

class Temperatura():
    @staticmethod
    def celsius_a_fahrenheit(grados_c):
        grados_f = 9.0/5.0 * grados_c + 32
        
        return grados_f
    
print(Temperatura.celsius_a_fahrenheit(50))
print(Temperatura.celsius_a_fahrenheit(22))
print(Temperatura.celsius_a_fahrenheit(0))