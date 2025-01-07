"""
    Crea una función palabra_mas_larga que reciba una lista de palabras y devuelva la palabra más larga de la lista.

    Pista avanzada:
        Puedes explorar la función max() con un argumento clave (key) para seleccionar elementos según su longitud.
"""


def palabra_mas_larga(lista):
    if not lista:
        return "La lista está vacía"

    max_len = max(lista,key=len)
    
    return max_len


print(palabra_mas_larga(["hola", "parque", "Bicentenario", "mermelada de frutilla"]))
print(palabra_mas_larga([]))


# Casco opcional si distintas palabras tienen misma longitud

def palabra_mas_larga_2(lista):
    if not lista:
        return "La lista está vacía"
    
    max_len = len(max(lista, key=len))  # Longitud de la palabra más larga
    palabras_largas = [palabra for palabra in lista if len(palabra) == max_len]
    return palabras_largas


print(palabra_mas_larga_2(["hola", "parque", "largo", "remera"]))  # Dos palabras con misma longitud
print(palabra_mas_larga_2([]))  # Lista vacía