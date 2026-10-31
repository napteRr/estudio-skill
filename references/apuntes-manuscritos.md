# Manejo de Apuntes Manuscritos y Escaneos

## 1. Orígenes habituales
- **Samsung Notes (PDF):** Trazos nítidos del S-Pen. Si viene en `.sdocx`, pedir al usuario exportar como PDF desde la app.
- **Adobe Scan (PDF/Imágenes):** Contraste optimizado y fondo blanco limpio.

## 2. Inspección Visual y Extracción
- Si el PDF escaneado tiene muchas páginas y la letra es apretada, rasterizar en alta resolución:
  `pdftoppm -png -r 150 <input.pdf> /tmp/pagina`
- Prestar atención a flechas, notas al margen, diagramas hechos a mano y llamadas de atención (*, ojo, examen).
- Deducir palabras dudosas a partir de la disciplina o marco teórico del tema.
