# TP Final - Ejercicio 3 - Punto A
# Pruebas unitarias de calcular_emisiones_carbono

import unittest

from emisiones import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):

    # caso normal: uso el factor por defecto (0.4)
    def test_calculo_con_factor_por_defecto(self):
        resultado = calcular_emisiones_carbono(100.0)
        self.assertEqual(resultado, 40.0)

    # caso normal: le paso yo el factor
    def test_calculo_con_factor_personalizado(self):
        resultado = calcular_emisiones_carbono(200.0, 0.5)
        self.assertEqual(resultado, 100.0)

    # caso borde: consumo cero, las emisiones tienen que ser cero
    def test_consumo_cero(self):
        resultado = calcular_emisiones_carbono(0.0)
        self.assertEqual(resultado, 0.0)

    # consumo con decimales (assertAlmostEqual por los decimales de los float)
    def test_consumo_con_decimales(self):
        resultado = calcular_emisiones_carbono(123.5, 0.4)
        self.assertAlmostEqual(resultado, 49.4)

    # consumo negativo: tiene que lanzar ValueError
    def test_consumo_negativo_lanza_error(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50.0)


if __name__ == "__main__":
    unittest.main()
