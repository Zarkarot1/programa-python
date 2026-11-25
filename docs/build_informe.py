#!/usr/bin/env python3
"""Genera el informe PDF de la Fase 5 a partir de un .docx con python-docx."""

from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from docx.opc.constants import RELATIONSHIP_TYPE as RT

BASE = Path(__file__).resolve().parent
PROY = BASE.parent
GITHUB_URL = "https://github.com/Zarkarot1/programa-python"
# Se reemplaza cuando el video esté publicado.
VIDEO_URL = ""

AZUL = RGBColor(0x14, 0x4A, 0x75)
GRIS = RGBColor(0x44, 0x44, 0x44)
NEGRO = RGBColor(0x1A, 0x1A, 0x1A)


def hipervinculo(parrafo, url: str, texto: str) -> None:
    """Agrega un hipervínculo real a un párrafo."""
    part = parrafo.part
    rid = part.relate_to(url, RT.HYPERLINK, is_external=True)
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), rid)
    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "144A75")
    subrayado = OxmlElement("w:u")
    subrayado.set(qn("w:val"), "single")
    rpr.append(color)
    rpr.append(subrayado)
    run.append(rpr)
    texto_xml = OxmlElement("w:t")
    texto_xml.text = texto
    run.append(texto_xml)
    hyperlink.append(run)
    parrafo._p.append(hyperlink)


def campo_pagina(parrafo) -> None:
    """Inserta el campo PAGE en el párrafo (número de página)."""
    run = parrafo.add_run()
    fld1 = OxmlElement("w:fldChar")
    fld1.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = "PAGE"
    fld2 = OxmlElement("w:fldChar")
    fld2.set(qn("w:fldCharType"), "end")
    run._r.append(fld1)
    run._r.append(instr)
    run._r.append(fld2)


def sombrear_celda(celda, color: str = "E8F0F8") -> None:
    sombra = OxmlElement("w:shd")
    sombra.set(qn("w:fill"), color)
    celda._tc.get_or_add_tcPr().append(sombra)


def bloque_codigo(doc: Document, texto: str, tamano: float = 8.0) -> None:
    parrafo = doc.add_paragraph()
    parrafo.paragraph_format.space_before = Pt(2)
    parrafo.paragraph_format.space_after = Pt(8)
    parrafo.paragraph_format.left_indent = Cm(0.4)
    parrafo.paragraph_format.line_spacing = 1.0
    run = parrafo.add_run(texto)
    run.font.name = "DejaVu Sans Mono"
    run.font.size = Pt(tamano)
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "DejaVu Sans Mono")
    # borde izquierdo y fondo
    ppr = parrafo._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr")
    left = OxmlElement("w:left")
    left.set(qn("w:val"), "single")
    left.set(qn("w:sz"), "18")
    left.set(qn("w:space"), "6")
    left.set(qn("w:color"), "144A75")
    bdr.append(left)
    ppr.append(bdr)
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), "F4F6F9")
    ppr.append(shd)


def tabla(doc: Document, encabezados: list[str], filas: list[list[str]],
          anchos_cm: list[float], tamano: float = 8.5) -> None:
    tabla_ = doc.add_table(rows=1, cols=len(encabezados))
    tabla_.style = "Table Grid"
    tabla_.alignment = WD_TABLE_ALIGNMENT.CENTER
    tabla_.autofit = False
    for i, ancho in enumerate(anchos_cm):
        for celda in tabla_.columns[i].cells:
            celda.width = Cm(ancho)
    for i, texto in enumerate(encabezados):
        celda = tabla_.rows[0].cells[i]
        celda.text = ""
        p = celda.paragraphs[0]
        run = p.add_run(texto)
        run.bold = True
        run.font.size = Pt(tamano)
        run.font.name = "DejaVu Sans"
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        sombrear_celda(celda)
    for fila_datos in filas:
        fila = tabla_.add_row()
        for i, texto in enumerate(fila_datos):
            celda = fila.cells[i]
            celda.text = ""
            p = celda.paragraphs[0]
            run = p.add_run(str(texto))
            run.font.size = Pt(tamano)
            run.font.name = "DejaVu Sans"
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    doc.add_paragraph()


def titulo(doc: Document, texto: str, nivel: int = 1) -> None:
    h = doc.add_heading(texto, level=nivel)
    for run in h.runs:
        run.font.name = "DejaVu Sans"
        run.font.color.rgb = AZUL
        run.font.bold = True


def parrafo(doc: Document, texto: str, *, justificar: bool = True,
            tamano: float = 10.5) -> None:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY if justificar else WD_ALIGN_PARAGRAPH.LEFT
    run = p.add_run(texto)
    run.font.name = "DejaVu Sans"
    run.font.size = Pt(tamano)


def construir() -> Path:
    doc = Document()

    # Estilos base
    normal = doc.styles["Normal"]
    normal.font.name = "DejaVu Sans"
    normal.font.size = Pt(10.5)
    normal.font.color.rgb = NEGRO
    for nivel in range(1, 4):
        estilo = doc.styles[f"Heading {nivel}"]
        estilo.font.name = "DejaVu Sans"
        estilo.font.color.rgb = AZUL

    seccion = doc.sections[0]
    seccion.page_width = Cm(21.0)
    seccion.page_height = Cm(29.7)
    seccion.top_margin = Cm(2.2)
    seccion.bottom_margin = Cm(2.0)
    seccion.left_margin = Cm(2.2)
    seccion.right_margin = Cm(2.2)

    # Encabezado y pie
    encabezado = seccion.header.paragraphs[0]
    encabezado.text = "Fase 5 - Evaluación Final POA · Fundamentos de Programación (213022)"
    encabezado.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    for run in encabezado.runs:
        run.font.size = Pt(8)
        run.font.name = "DejaVu Sans"
        run.font.color.rgb = GRIS
    pie = seccion.footer.paragraphs[0]
    pie.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_pie = pie.add_run("Página ")
    run_pie.font.size = Pt(8)
    run_pie.font.name = "DejaVu Sans"
    run_pie.font.color.rgb = GRIS
    campo_pagina(pie)

    # ------------------------- Portada -------------------------
    for _ in range(5):
        doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Solución del Problema 1:")
    r.bold = True
    r.font.size = Pt(24)
    r.font.color.rgb = AZUL
    r.font.name = "DejaVu Sans"
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("clasificación del compromiso de sesiones")
    r.bold = True
    r.font.size = Pt(20)
    r.font.color.rgb = AZUL
    r.font.name = "DejaVu Sans"
    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Fase 5 - Evaluación Final POA\nFundamentos de Programación (213022)")
    r.font.size = Pt(13)
    r.font.color.rgb = GRIS
    r.font.name = "DejaVu Sans"
    for _ in range(5):
        doc.add_paragraph()
    for texto, tamano in [
        ("Rubén Dario Lozano Contreras", 14),
        ("Grupo: 213022_974", 11.5),
        ("Ingeniería en Inteligencia Artificial y Ciencia de Datos", 11.5),
        ("Tutor: Alfredo Jesús Castro Guzman", 11.5),
    ]:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(texto)
        r.font.size = Pt(tamano)
        r.font.name = "DejaVu Sans"
        if tamano == 14:
            r.bold = True
    for _ in range(5):
        doc.add_paragraph()
    for texto in [
        "Universidad Nacional Abierta y a Distancia - UNAD",
        "Escuela de Ciencias Básicas, Tecnología e Ingeniería - ECBTI",
        "Noviembre de 2026",
    ]:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(texto)
        r.font.size = Pt(11)
        r.font.name = "DejaVu Sans"
        r.font.color.rgb = GRIS
    doc.add_page_break()

    # --------------------- 1. Problema ---------------------
    titulo(doc, "1. Problema elegido")
    parrafo(doc, "El banco de problemas de la Fase 5 propone elegir un problema y "
                 "resolverlo en Python. Elegí el Problema 1: una matriz almacena "
                 "sesiones de clientes de una plataforma digital con el formato "
                 "[ID del cliente, duración de la sesión (segundos), número de "
                 "clics]. Se debe evaluar el nivel de compromiso de cada sesión y "
                 "mostrar un informe con el ID y su clasificación final.")
    parrafo(doc, "Las reglas del negocio son tres:")
    for texto in [
        "Alto: duración mayor que 180 segundos y más de 8 clics.",
        "Bajo: duración menor que 60 segundos o menos de 3 clics.",
        "Medio: cualquier otro caso.",
    ]:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(texto)
        r.font.name = "DejaVu Sans"
        r.font.size = Pt(10.5)

    # --------------------- 2. Requerimientos ---------------------
    titulo(doc, "2. Tabla de requerimientos")
    tabla(doc,
          ["ID", "Requerimiento", "Entrada / proceso", "Criterio de aceptación"],
          [
              ["R1", "Crear la matriz de sesiones",
               "Al menos 5 filas con 3 columnas numéricas",
               "La matriz tiene 7 sesiones válidas"],
              ["R2", "Clasificar una sesión",
               "Duración y clics → función de clasificación",
               "Devuelve Alto, Medio o Bajo según las reglas"],
              ["R3", "Validar los datos",
               "Comprobar columnas y enteros no negativos",
               "Datos inválidos lanzan ValueError"],
              ["R4", "Generar el informe",
               "Recorrer la matriz y clasificar cada fila",
               "Aparecen todos los ID en orden"],
              ["R5", "Mostrar el informe",
               "Formatear tabla con encabezado y totales",
               "Salida legible en consola"],
              ["R6", "Ejecutar el programa",
               "main() con guarda __main__",
               "Termina sin errores"],
          ],
          [1.2, 4.4, 5.6, 5.4])

    # --------------------- 3. Diseño ---------------------
    titulo(doc, "3. Diseño de la solución")
    titulo(doc, "3.1 Pseudocódigo", nivel=2)
    bloque_codigo(doc, """INICIO
  matriz <- [[1001,240,12], [1002,180,9], ...]
  PARA cada fila EN matriz HACER
    validar fila (3 columnas, enteros no negativos)
    SI duración > 180 Y clics > 8 ENTONCES
      clasificación <- "Alto"
    SINO SI duración < 60 O clics < 3 ENTONCES
      clasificación <- "Bajo"
    SINO
      clasificación <- "Medio"
    FIN SI
    agregar (ID, clasificación) al informe
  FIN PARA
  mostrar informe
FIN""")

    titulo(doc, "3.2 Diagrama de flujo", nivel=2)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(str(PROY / "docs" / "diagrama_flujo.png"), width=Cm(12.4))
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Figura 1. Diagrama de flujo de la clasificación de compromiso.")
    r.italic = True
    r.font.size = Pt(8.5)
    r.font.name = "DejaVu Sans"
    doc.add_page_break()

    # --------------------- 4. Código ---------------------
    titulo(doc, "4. Explicación del código")
    parrafo(doc, "El programa se organiza en funciones pequeñas, cada una con una "
                 "responsabilidad:")
    for texto in [
        "clasificar_compromiso(duracion, clics): valida los tipos y aplica las tres "
        "reglas en orden. Primero comprueba Alto; si no, Bajo; y si tampoco, Medio.",
        "validar_sesion(sesion): verifica que la fila tenga tres datos y que el ID "
        "sea entero; delega la validación de duración y clics.",
        "generar_informe(sesiones): recorre la matriz con un ciclo y construye la "
        "lista de tuplas (ID, clasificación).",
        "formatear_informe(informe): arma la tabla de salida y cuenta cuántas "
        "sesiones hay por clasificación.",
        "main(): punto de entrada; llama a las funciones y muestra el informe.",
    ]:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(texto)
        r.font.name = "DejaVu Sans"
        r.font.size = Pt(10.5)
    parrafo(doc, "Se usan estructuras de control (if/elif/else), una estructura "
                 "repetitiva (for), listas, tuplas, funciones y validación de datos. "
                 "No se usan librerías externas.")

    # --------------------- 5. Pruebas ---------------------
    titulo(doc, "5. Pruebas de escritorio")
    tabla(doc,
          ["#", "Duración (s)", "Clics", "Condición", "Esperado", "Obtenido"],
          [
              ["1", "240", "12", "240 > 180 y 12 > 8", "Alto", "Alto"],
              ["2", "180", "9", "180 no es > 180", "Medio", "Medio"],
              ["3", "181", "8", "8 no es > 8", "Medio", "Medio"],
              ["4", "59", "10", "59 < 60", "Bajo", "Bajo"],
              ["5", "200", "2", "2 < 3", "Bajo", "Bajo"],
              ["6", "60", "3", "Límites inferiores exactos", "Medio", "Medio"],
              ["7", "300", "20", "300 > 180 y 20 > 8", "Alto", "Alto"],
              ["8", "-1", "5", "Duración negativa", "ValueError", "ValueError"],
          ],
          [1.0, 2.2, 1.6, 4.6, 2.8, 2.8])

    # --------------------- 6. Evidencia ---------------------
    titulo(doc, "6. Evidencia de ejecución")
    bloque_codigo(doc, """INFORME DE COMPROMISO DE SESIONES
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
Total de sesiones: 7 | Alto: 2, Bajo: 2, Medio: 3""")

    # --------------------- 7. Enlaces ---------------------
    titulo(doc, "7. Enlaces de la entrega")
    parrafo(doc, "Repositorio público de GitHub:", justificar=False)
    p = doc.add_paragraph()
    hipervinculo(p, GITHUB_URL, GITHUB_URL)
    parrafo(doc, "Video de sustentación en YouTube:", justificar=False)
    p = doc.add_paragraph()
    if VIDEO_URL:
        hipervinculo(p, VIDEO_URL, VIDEO_URL)
    else:
        r = p.add_run("Pendiente de publicación (se actualizará antes de la entrega).")
        r.font.name = "DejaVu Sans"
        r.font.size = Pt(10.5)
        r.font.color.rgb = RGBColor(0xB0, 0x2A, 0x37)

    # --------------------- 8. Conclusiones ---------------------
    titulo(doc, "8. Conclusiones")
    parrafo(doc, "La solución cumple el problema porque separa la lógica de "
                 "clasificación de la entrada y de la salida, valida los datos y "
                 "respeta los límites exactos de las reglas. Las pruebas de "
                 "escritorio y las pruebas automáticas confirman los casos normales "
                 "y de frontera. El ejercicio permitió aplicar condicionales, "
                 "ciclos, listas, funciones y validación, que son los temas "
                 "evaluados en la Fase 5.")

    # --------------------- 9. Referencias ---------------------
    titulo(doc, "9. Referencias")
    referencias = [
        "Ceballos Sierra, F. J. (2015). C/C++. Curso de programación (4.ª ed.). "
        "Ra-Ma. https://elibro-net.bibliotecavirtual.unad.edu.co/es/ereader/unad/106454",
        "Deitel, P., & Deitel, H. (2016). Cómo programar en C/C++. Pearson Educación.",
        "GitHub, Inc. (2025). Acerca de GitHub y Git. GitHub Docs. "
        "https://docs.github.com/es/get-started/start-your-journey/about-github-and-git",
        "Python Software Foundation. (2025). The Python Tutorial. "
        "https://docs.python.org/3/tutorial/",
        "Universidad Nacional Abierta y a Distancia. (2026). Guía de aprendizaje - "
        "Fase 5 Evaluación Final POA. Curso Fundamentos de Programación (213022).",
    ]
    for ref in referencias:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(0.8)
        p.paragraph_format.first_line_indent = Cm(-0.8)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(ref)
        r.font.name = "DejaVu Sans"
        r.font.size = Pt(9.5)

    # --------------------- Anexo código ---------------------
    doc.add_page_break()
    titulo(doc, "Anexo A. Código fuente completo")
    codigo = (PROY / "solucion_problema_1.py").read_text(encoding="utf-8")
    for linea in codigo.splitlines():
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        r = p.add_run(linea if linea else " ")
        r.font.name = "DejaVu Sans Mono"
        r.font.size = Pt(7.6)

    # Propiedades del documento: solo autoría
    props = doc.core_properties
    props.author = "Rubén Dario Lozano Contreras"
    props.last_modified_by = "Rubén Dario Lozano Contreras"
    props.title = ""
    props.subject = ""
    props.keywords = ""
    props.comments = ""
    props.category = ""

    salida = PROY / "docs" / "Informe_Fase5_RubenDarioLozanoContreras.docx"
    doc.save(str(salida))
    return salida


if __name__ == "__main__":
    print(construir())
