---
name: estudio
description: Suite integral de estudio universitario. Procesa apuntes de cátedra (incluyendo manuscritos de Samsung Notes y Adobe Scan) y genera PDFs independientes según elección del usuario: 1. Resumen Multinivel, 2. Método Feynman y 3. Modelo de Parcial con Active Recall. Usar cuando el usuario pida estudiar un tema, resumir apuntes de facultad, preparar parciales o mencione 'estudio'.
---

# Suite de Estudio Universitario

Flujo optimizado para transformar apuntes de clase, lecturas densas o notas manuscritas en material de estudio de alta retención.

## Flujo de Ejecución Obligatorio

### 1. Interrogatorio de Formatos (Paso Previo Indispensable)
Al recibir el material (texto, fotos o PDF de notas), NO generes directamente un resumen. Pregunta al usuario cuáles de las siguientes opciones necesita generar:

1. **Resumen Multinivel** (`academic-summarizer`): Ficha panorámica, tesis, desarrollo analítico por ejes, cuadros comparativos y glosario de cátedra.
2. **Método Feynman** (`feynman-explainer`): Conceptos difíciles explicados sin jerga, analogías del mundo real, mecanismos paso a paso y puente a la respuesta de examen.
3. **Modelo de Parcial y Active Recall** (`active-recall-exam`): Simulacro de examen con preguntas conceptuales, casos prácticos, trampas comunes y rúbricas para un 10.

> **Regla de salida:** Cada opción seleccionada debe compilarse en un **archivo PDF independiente**. Si el usuario elige las 3, genera **3 PDFs separados**.

---

### 2. Procesamiento y Redacción
Consulta las especificaciones de cada metodología en [metodologias.md](./references/metodologias.md):
- Si el material proviene de Samsung Notes o escaneos a mano, sigue las pautas de [apuntes-manuscritos.md](./references/apuntes-manuscritos.md).
- Redacta cada documento en Markdown cuidando la jerarquía visual, tablas y bloques destacados (`>`).

---

### 3. Compilación a PDF
Usa el script auxiliar provisto en [generar_pdf.py](./scripts/generar_pdf.py):

```bash
# Para Resumen Multinivel:
python3 scripts/generar_pdf.py <archivo.md> "[Materia] - Resumen Multinivel - [Tema].pdf" multinivel

# Para Método Feynman:
python3 scripts/generar_pdf.py <archivo.md> "[Materia] - Metodo Feynman - [Tema].pdf" feynman

# Para Modelo de Parcial:
python3 scripts/generar_pdf.py <archivo.md> "[Materia] - Modelo de Parcial - [Tema].pdf" parcial
```

En entornos sin terminal o interfaces de chat web, entrega el código HTML estilizado para que el usuario imprima a PDF con `Ctrl + P`.
