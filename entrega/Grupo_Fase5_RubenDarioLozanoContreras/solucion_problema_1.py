"""Fase 5 - Evaluación Final POA (Fundamentos de Programación, 213022).

Problema 1: clasificar el compromiso de las sesiones de una plataforma
digital a partir de su duración y su número de clics.

Formato de cada fila de la matriz:
    [ID del cliente, duración de la sesión (segundos), número de clics]

Reglas:
    Alto  -> duración > 180 s  y  clics > 8
    Bajo  -> duración < 60 s   o  clics < 3
    Medio -> cualquier otro caso

Autor: Rubén Dario Lozano Contreras
Grupo: 213022_974
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence

# Matriz con 7 sesiones (el problema exige mínimo 5).
# Incluye casos normales y de frontera para las pruebas.
MATRIZ_SESIONES: list[list[int]] = [
    [1001, 240, 12],   # Alto
    [1002, 180, 9],    # Medio: la duración no es estrictamente mayor que 180
    [1003, 181, 8],    # Medio: los clics no son estrictamente mayores que 8
    [1004, 59, 10],    # Bajo: duración menor que 60
    [1005, 200, 2],    # Bajo: clics menores que 3
    [1006, 60, 3],     # Medio: justo en los límites inferiores
    [1007, 300, 20],   # Alto
]

DURACION_ALTA = 180
CLICS_ALTOS = 8
DURACION_BAJA = 60
CLICS_BAJOS = 3


def clasificar_compromiso(duracion: int, clics: int) -> str:
    """Devuelve 'Alto', 'Medio' o 'Bajo' según duración y clics.

    Lanza ValueError si los datos no son enteros no negativos.
    """
    if isinstance(duracion, bool) or not isinstance(duracion, int):
        raise ValueError("La duración debe ser un número entero.")
    if isinstance(clics, bool) or not isinstance(clics, int):
        raise ValueError("El número de clics debe ser un número entero.")
    if duracion < 0 or clics < 0:
        raise ValueError("La duración y los clics no pueden ser negativos.")

    if duracion > DURACION_ALTA and clics > CLICS_ALTOS:
        return "Alto"
    if duracion < DURACION_BAJA or clics < CLICS_BAJOS:
        return "Bajo"
    return "Medio"


def validar_sesion(sesion: Sequence[int]) -> tuple[int, int, int]:
    """Valida una fila de la matriz y la devuelve como tupla de tres enteros."""
    if len(sesion) != 3:
        raise ValueError(
            f"La sesión debe tener 3 datos [ID, duración, clics]: {sesion!r}")
    identificador, duracion, clics = sesion
    if isinstance(identificador, bool) or not isinstance(identificador, int):
        raise ValueError(f"El ID del cliente debe ser entero: {identificador!r}")
    clasificar_compromiso(duracion, clics)  # valida duración y clics
    return identificador, duracion, clics


def generar_informe(sesiones: Iterable[Sequence[int]]) -> list[tuple[int, str]]:
    """Recorre la matriz y devuelve [(ID, clasificación), ...]."""
    informe: list[tuple[int, str]] = []
    for sesion in sesiones:
        identificador, duracion, clics = validar_sesion(sesion)
        informe.append((identificador, clasificar_compromiso(duracion, clics)))
    return informe


def formatear_informe(informe: list[tuple[int, str]]) -> str:
    """Devuelve el informe como texto tabulado con encabezado y totales."""
    lineas = [
        "INFORME DE COMPROMISO DE SESIONES",
        "=" * 40,
        f"{'ID del cliente':<16}{'Clasificación':>16}",
        "-" * 40,
    ]
    for identificador, clasificacion in informe:
        lineas.append(f"{identificador:<16}{clasificacion:>16}")
    lineas.append("-" * 40)
    conteo: dict[str, int] = {}
    for _, clasificacion in informe:
        conteo[clasificacion] = conteo.get(clasificacion, 0) + 1
    resumen = ", ".join(f"{clave}: {valor}" for clave, valor in sorted(conteo.items()))
    lineas.append(f"Total de sesiones: {len(informe)} | {resumen}")
    return "\n".join(lineas)


def main() -> None:
    """Punto de entrada: genera e imprime el informe de la matriz."""
    informe = generar_informe(MATRIZ_SESIONES)
    print(formatear_informe(informe))


if __name__ == "__main__":
    main()
