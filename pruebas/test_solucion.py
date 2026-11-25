"""Pruebas del Problema 1: casos normales, límites y errores."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solucion_problema_1 import (  # noqa: E402
    MATRIZ_SESIONES,
    clasificar_compromiso,
    formatear_informe,
    generar_informe,
    validar_sesion,
)


class ClasificacionTest(unittest.TestCase):
    def test_alto(self):
        self.assertEqual(clasificar_compromiso(181, 9), "Alto")
        self.assertEqual(clasificar_compromiso(240, 12), "Alto")

    def test_medio_por_limites(self):
        self.assertEqual(clasificar_compromiso(180, 9), "Medio")
        self.assertEqual(clasificar_compromiso(181, 8), "Medio")
        self.assertEqual(clasificar_compromiso(60, 3), "Medio")
        self.assertEqual(clasificar_compromiso(120, 5), "Medio")

    def test_bajo(self):
        self.assertEqual(clasificar_compromiso(59, 10), "Bajo")
        self.assertEqual(clasificar_compromiso(200, 2), "Bajo")
        self.assertEqual(clasificar_compromiso(0, 0), "Bajo")

    def test_datos_invalidos(self):
        with self.assertRaises(ValueError):
            clasificar_compromiso(-1, 5)
        with self.assertRaises(ValueError):
            clasificar_compromiso(200, -1)
        with self.assertRaises(ValueError):
            clasificar_compromiso("200", 5)  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            clasificar_compromiso(200, 5.5)  # type: ignore[arg-type]


class InformeTest(unittest.TestCase):
    def test_matriz_minima(self):
        self.assertGreaterEqual(len(MATRIZ_SESIONES), 5)

    def test_informe_completo(self):
        informe = generar_informe(MATRIZ_SESIONES)
        self.assertEqual(len(informe), len(MATRIZ_SESIONES))
        self.assertEqual(
            informe,
            [
                (1001, "Alto"),
                (1002, "Medio"),
                (1003, "Medio"),
                (1004, "Bajo"),
                (1005, "Bajo"),
                (1006, "Medio"),
                (1007, "Alto"),
            ],
        )

    def test_formato(self):
        texto = formatear_informe(generar_informe(MATRIZ_SESIONES))
        self.assertIn("ID del cliente", texto)
        self.assertIn("Clasificación", texto)
        self.assertIn("Total de sesiones: 7", texto)

    def test_sesion_con_columnas_incorrectas(self):
        with self.assertRaises(ValueError):
            validar_sesion([1001, 200])  # type: ignore[list-item]


if __name__ == "__main__":
    unittest.main()
