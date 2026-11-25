# Tabla de requerimientos — Problema 1

| ID | Requerimiento | Entrada | Proceso | Salida | Criterio de aceptación |
|---|---|---|---|---|---|
| R1 | Crear la matriz de sesiones | — | Definir al menos 5 filas `[ID, duración, clics]` | Matriz de sesiones | La matriz tiene 7 filas con tres datos numéricos cada una |
| R2 | Calcular la clasificación de una sesión | Duración y clics | Función que aplica las reglas Alto/Medio/Bajo | `"Alto"`, `"Medio"` o `"Bajo"` | Los límites exactos se respetan: 180 s y 8 clics no son Alto; 60 s y 3 clics no son Bajo |
| R3 | Validar los datos de entrada | Fila de la matriz | Comprobar tres columnas y números enteros no negativos | Error `ValueError` o tupla válida | Datos inválidos generan error; datos válidos se procesan |
| R4 | Generar el informe | Matriz completa | Recorrer la matriz con un ciclo y clasificar cada sesión | Lista de `(ID, clasificación)` | Aparecen todos los IDs de la matriz, en orden |
| R5 | Mostrar el informe | Lista de resultados | Formatear una tabla con encabezado y totales | Texto en consola | La salida muestra ID, clasificación y total de sesiones |
| R6 | Ejecutar el programa | — | `main()` con `if __name__ == "__main__"` | Salida sin errores | `python3 solucion_problema_1.py` termina con código 0 |
