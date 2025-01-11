"""
    Crea una función calculadora(a, b, operacion) que soporte las siguientes operaciones: suma, resta, multiplicación y división. 
    Escribe pruebas para validar el correcto funcionamiento de la función y asegúrate de incluir pruebas para manejar divisiones por cero.

    Requisitos del ejercicio:

    Pruebas para cada operación matemática.
    Verificación de la excepción cuando se intenta dividir por cero.
    Asegurar que se lanza una excepción para operaciones no válidas.
"""

import unittest


def calculadora(a, b, operacion):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplicacion":
        return a * b
    elif operacion == "division":
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b
    else:
        raise ValueError("Operación no válida")
    


class TestCalculadora(unittest.TestCase):
    def test_suma_valida(self):
        self.assertEqual(calculadora(1,5,"suma"),6)

    def test_resta_valida(self):
        self.assertEqual(calculadora(5,1,"resta"),4)

    def test_multiplicacion_valida(self):
        self.assertEqual(calculadora(1,5,"multiplicacion"),5)

    def test_division_valida(self):
        self.assertEqual(calculadora(10,2,"division"),5)

    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            calculadora(10,0,"division")

    def test_operacion_invalida(self):
        with self.assertRaises(ValueError):
            calculadora(1,2,"multiplicar")



if __name__ == "__main__":
    unittest.main()