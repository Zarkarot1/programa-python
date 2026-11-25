# Pruebas de escritorio — Problema 1

| # | Duración (s) | Clics | Condición evaluada | Resultado esperado | Resultado obtenido |
|---|---|---|---|---|---|
| 1 | 240 | 12 | 240 > 180 y 12 > 8 | Alto | Alto |
| 2 | 180 | 9 | 180 no es > 180; 9 > 8 | Medio | Medio |
| 3 | 181 | 8 | 181 > 180 pero 8 no es > 8 | Medio | Medio |
| 4 | 59 | 10 | 59 < 60 | Bajo | Bajo |
| 5 | 200 | 2 | 2 < 3 | Bajo | Bajo |
| 6 | 60 | 3 | 60 no es < 60; 3 no es < 3; no cumple Alto | Medio | Medio |
| 7 | 300 | 20 | 300 > 180 y 20 > 8 | Alto | Alto |
| 8 | -1 | 5 | Duración negativa | `ValueError` | `ValueError` |

Las pruebas automáticas de `pruebas/test_solucion.py` verifican los mismos casos
con `unittest`.
