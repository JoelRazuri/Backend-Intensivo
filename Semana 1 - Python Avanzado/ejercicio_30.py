"""
    Implementa un generador infinito contador_infinito() que devuelva números incrementales empezando desde 1.  
"""

def contador_infinito():
    contador = 1
    
    while True:
        yield contador
        contador+=1


gen = contador_infinito()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))