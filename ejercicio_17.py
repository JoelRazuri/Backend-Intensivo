"""
    Palabras que contienen la letra 'a': De una lista de palabras ["python", "java", "c", "javascript", "c++"], genera una lista de las palabras que 
    contienen la letra 'a'.
"""

palabras = ["python", "java", "c", "javascript", "c++"]

cotienen_a = [palabra for palabra in palabras if 'a' in palabra]

print(cotienen_a)