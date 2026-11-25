# Guion de sustentación — Fase 5 (máximo 10 minutos)

**Título exacto del video:** `Sustentación Fase 5 – Rubén Dario Lozano Contreras`
**Descripción:** Solución en Python del Problema 1 de la Fase 5: clasificación del
compromiso de sesiones con matriz, funciones, condicionales y pruebas.
**Duración objetivo:** 8 min 30 s (máximo 10 min).

## Antes de grabar

- Ten a mano el **documento de identidad** con el **nombre visible** y el
  **número tapado** (cinta o dedo). No se debe ver el número.
- Abre el código `solucion_problema_1.py` y una terminal en la carpeta del proyecto.
- Ten abierta la página del repositorio: https://github.com/Zarkarot1/programa-python
- Graba en horizontal, con buena luz y audio; comparte pantalla cuando expliques el código.
- Ten el cronómetro visible. No superes los 10 minutos.

## Guion cronometrado

### 0:00 – 0:40 · Presentación e identidad
“Buenos días, tutor. Mi nombre es **Rubén Dario Lozano Contreras**, del grupo
**213022_974**, del programa **Ingeniería en Inteligencia Artificial y Ciencia de
Datos**, del centro **Gachetá**. A continuación muestro mi documento de identidad
con mi nombre visible y el número cubierto, como mecanismo de validación.”
*(Muestra el documento a cámara durante 3–5 segundos; el número debe estar tapado).*

“En este video explico la solución en Python del **Problema 1** de la Fase 5.”

### 0:40 – 1:35 · El problema
“El problema parte de una matriz de sesiones de clientes. Cada fila tiene tres
datos: **ID del cliente, duración en segundos y número de clics**. Hay que
clasificar el compromiso de cada sesión así: **Alto** si dura más de 180 segundos
y tiene más de 8 clics; **Bajo** si dura menos de 60 segundos o tiene menos de 3
clics; y **Medio** en cualquier otro caso. La salida debe listar el ID y su
clasificación.”

### 1:35 – 2:30 · Requerimientos
“Antes de programar, definí seis requerimientos: R1, crear una matriz con al menos
cinco sesiones; R2, una función que clasifique; R3, validar los datos; R4,
recorrer la matriz y generar el informe; R5, mostrar la tabla con totales; y R6,
ejecutar todo desde `main`. Los criterios de aceptación están en el informe: por
ejemplo, que los límites exactos se respeten.”

### 2:30 – 3:40 · Lógica y casos de frontera
“La parte crítica son los operadores estrictos. **180 segundos no es Alto**,
porque la regla dice *mayor que* 180; **8 clics tampoco es Alto**, porque dice
*más de* 8. Y **60 segundos no es Bajo**, porque dice *menor que* 60; **3 clics
tampoco**. Por eso los casos de frontera se van a Medio. Esto lo probé con los
siete registros de la matriz y con casos límite.”

### 3:40 – 4:40 · Diagrama de flujo
“El diagrama muestra el flujo: se lee la matriz, se valida cada fila, se pregunta
primero si cumple Alto; si no, se pregunta si cumple Bajo; si tampoco, se asigna
Medio. Luego se agrega el par ID-clasificación al informe y se repite hasta
terminar. Al final se muestra el informe.”

### 4:40 – 6:30 · Código
*(Comparte pantalla y recorre el archivo).*
“El programa tiene cinco funciones. `clasificar_compromiso` concentra las reglas.
`validar_sesion` comprueba que la fila tenga tres columnas y que los datos sean
enteros no negativos. `generar_informe` recorre la matriz con un `for` y construye
la lista de tuplas. `formatear_informe` arma la tabla y cuenta las clasificaciones.
Y `main` es el punto de entrada, protegido con `if __name__ == "__main__"`.
Así separo entrada, lógica y salida, y puedo probar la función sin depender de la
impresión en pantalla.”

### 6:30 – 7:30 · Pruebas
“Ejecuto las pruebas automáticas con `unittest`: son ocho pruebas. Cubren Alto,
Medio y Bajo, los límites exactos y los datos inválidos, como una duración
negativa o un tipo de dato incorrecto. También hice la prueba de escritorio con
los mismos casos. El programa responde lo esperado.”

### 7:30 – 8:20 · Repositorio y ejecución
“El código está en el repositorio público de GitHub:
**github.com/Zarkarot1/programa-python**. Allí están el programa, el README y las
pruebas. Ejecuto `python3 solucion_problema_1.py` y muestro la salida: los siete
IDs con su clasificación y el total.”

### 8:20 – 9:00 · Cierre
“Con esto se cumple el problema: la matriz tiene siete sesiones, la clasificación
respeta los límites, el informe se genera y las pruebas lo confirman. Aprendí a
separar la lógica en funciones y a probar los casos de frontera, que es donde
suelen aparecer los errores. Muchas gracias.”

## Checklist final del video

- [ ] Nombre completo y documento con el **número oculto**.
- [ ] Grupo, programa y centro mencionados.
- [ ] Título exacto: `Sustentación Fase 5 – Rubén Dario Lozano Contreras`.
- [ ] Descripción con el resumen de la solución.
- [ ] Enlace accesible sin iniciar sesión.
- [ ] Duración menor a 10 minutos.
