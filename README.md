# 🎓 Estudio Skill — Suite Integral de Estudio Universitario

Una skill para agentes de Inteligencia Artificial (**Antigravity**, **Claude Code**, **Cursor**, **ChatGPT**, etc.) diseñada para procesar apuntes de clase, lecturas densas y notas manuscritas (Samsung Notes, Adobe Scan), transformándolas en material pedagógico de alta retención.

Construida siguiendo las mejores prácticas oficiales de diseño de skills (**`skill-creator` / `writing-skills`**) con arquitectura de divulgación progresiva (*Progressive Disclosure*).

🔗 **Repositorio:** [github.com/napteRr/estudio-skill](https://github.com/napteRr/estudio-skill)

---

## ⚡ ¿Cómo funciona?

Cuando le pides a tu agente:
> *"Che, usá esta skill y haceme un resumen de [Materia / Tema]"*

El agente **no genera un resumen genérico**. Primero te pregunta cuáles de los siguientes formatos deseas generar:

| Formato | Metodología | Resultado |
| :--- | :--- | :--- |
| **1. Resumen Multinivel** | `academic-summarizer` | Ficha panorámica, tesis principal, desarrollo por ejes, cuadros comparativos y glosario técnico de cátedra. |
| **2. Método Feynman** | `feynman-explainer` | Conceptos difíciles explicados sin jerga, analogías de la vida real, mecanismo paso a paso y traducción al vocabulario de examen. |
| **3. Modelo de Parcial** | `active-recall-exam` | Simulacro de examen con preguntas conceptuales, de desarrollo, casos prácticos, cazabobos y rúbricas para un 10. |

> 📌 **Regla de oro:** Si seleccionas más de una opción (o las tres), la skill compila **archivos PDF independientes y separados** para cada una, con paleta de colores y estilos editoriales diferenciados.

---

## ✍️ Compatibilidad con Apuntes Manuscritos

- **Samsung Notes:** Compatible con PDFs exportados del S-Pen (se recomienda *Compartir/Guardar como PDF*).
- **Adobe Scan:** Reconocimiento de alta fidelidad con contraste y alineación automática.
- Lectura multimodal directa de caligrafía rápida, tachones, esquemas a mano y notas al margen.

---

## 🚀 Instalación Rápida con GitHub

Cualquier persona puede instalar esta skill en su máquina clonando directamente desde GitHub:

### 1. Global para Antigravity (todos los proyectos)
```bash
git clone https://github.com/napteRr/estudio-skill.git ~/.gemini/config/skills/estudio
```

### 2. Global para Claude Code
```bash
git clone https://github.com/napteRr/estudio-skill.git ~/.claude/skills/estudio
```

### 3. En un proyecto específico (Cursor / Antigravity / Claude Code)
Dentro de la carpeta de tu materia o proyecto:
```bash
mkdir -p .agents/skills
git clone https://github.com/napteRr/estudio-skill.git .agents/skills/estudio
```

### 4. En interfaces Web (ChatGPT / Claude.ai)
No requiere terminal: simplemente descarga el repositorio o adjunta directamente el archivo [**`SKILL.md`**](https://raw.githubusercontent.com/napteRr/estudio-skill/main/SKILL.md) junto a tus apuntes en la conversación.

---

## 📦 Estructura del Repositorio

```text
estudio-skill/
├── SKILL.md                  # Especificación principal con frontmatter YAML
├── scripts/
│   └── generar_pdf.py        # Motor de compilación a PDF con estilos CSS
├── references/
│   ├── metodologias.md       # Especificación pedagógica de los 3 formatos
│   └── apuntes-manuscritos.md # Pautas de visión y rasterizado en alta resolución
├── LICENSE                   # Licencia MIT
└── README.md
```

---

## 🛠️ Requisitos para Exportar a PDF (Opcional)

Si utilizas un entorno con terminal y deseas compilar automáticamente los PDFs con diseño académico:
- **Python 3** con el paquete `markdown` (`pip install markdown`).
- **LibreOffice** (`libreoffice --headless`).

*(En caso de no contar con LibreOffice, la skill genera código HTML/Markdown listo para guardar como PDF desde el navegador con `Ctrl + P`).*

---

## 📄 Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).
