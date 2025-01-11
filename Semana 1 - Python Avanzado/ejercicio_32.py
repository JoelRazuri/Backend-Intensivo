"""
    Crea una función guardar_datos_json(nombre_archivo, datos) que guarde un diccionario en un archivo JSON. 
    Luego, escribe una función cargar_datos_json(nombre_archivo) que lea y devuelva los datos del archivo.

    Requisitos del ejercicio:

    Guardar el diccionario en un archivo llamado datos.json.
    Leer los datos del archivo y asegurarte de que se carguen correctamente.
    Verificar que el tipo de datos cargado sea un diccionario.
"""
import json

datos = {
    "nombre": "Joel",
    "edad": 25,
    "lenguajes": ["Python", "Django", "JavaScript"]
}


def guardar_datos_json(nombre_archivo, datos):
    try:
        with open(nombre_archivo, "w") as archivo:
            json.dump(datos, archivo, indent=4)

        print("Archivo creado exitosamente")
    except (IOError, TypeError) as e:
        print(f"Error al crear el archivo: {e}")


def cargar_datos_json(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            datos_cargados = json.load(archivo)

        print("Datos cargados exitosamente: ", datos_cargados)
        
        if isinstance(datos_cargados, dict):
            print("Los datos cargados son un diccionario.")
        else:
            print("Los datos cargados no son un diccionario.")
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error al leer el archivo: {e}")

guardar_datos_json("datos.json", datos)
cargar_datos_json("datos.json")
