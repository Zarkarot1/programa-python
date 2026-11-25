# Fase 5 — Evaluación Final POA (Problema 1)

Solución en Python del **Problema 1** del banco de problemas de la Fase 5 del
curso **Fundamentos de Programación (213022)** de la UNAD.

## Problema

Una matriz almacena sesiones de clientes en una plataforma digital:

```text
[ID del cliente, duración de la sesión (segundos), número de clics]
```

Se debe clasificar el compromiso de cada sesión:

- **Alto:** duración **> 180 s** y clics **> 8**.
- **Bajo:** duración **< 60 s** o clics **< 3**.
- **Medio:** cualquier otro caso.

La salida lista el ID del cliente y su clasificación.

## Estructura

```
.
├── solucion_problema_1.py     # programa principal
├── pruebas/
│   └── test_solucion.py       # 8 pruebas con unittest
└── README.md
```

## Uso

Requiere Python 3.10 o superior. No usa librerías externas.

```bash
python3 solucion_problema_1.py
```

Salida esperada:

```text
INFORME DE COMPROMISO DE SESIONES
========================================
ID del cliente     Clasificación
----------------------------------------
1001                        Alto
1002                       Medio
1003                       Medio
1004                        Bajo
1005                        Bajo
1006                       Medio
1007                        Alto
----------------------------------------
Total de sesiones: 7 | Alto: 2, Bajo: 2, Medio: 3
```

## Pruebas

```bash
python3 -m unittest discover -s pruebas -v
```

Cubren clasificación Alta/Media/Baja, los límites exactos (180 s, 8 clics,
60 s, 3 clics), datos inválidos y el formato del informe.

## Autor

Rubén Dario Lozano Contreras — Grupo 213022_974
Curso: Fundamentos de Programación (213022) — UNAD
