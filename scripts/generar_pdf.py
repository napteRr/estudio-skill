import sys, os, markdown, subprocess

def md_to_pdf(md_path, pdf_path, doc_type="multinivel"):
    if not os.path.exists(md_path):
        print(f"Error: No existe {md_path}")
        return False
        
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Themes
    themes = {
        "multinivel": {
            "primary": "#1e3a8a",
            "secondary": "#2563eb",
            "bg_box": "#eff6ff",
            "border_box": "#3b82f6",
            "badge": "RESUMEN MULTINIVEL"
        },
        "feynman": {
            "primary": "#4338ca",
            "secondary": "#6366f1",
            "bg_box": "#f5f3ff",
            "border_box": "#8b5cf6",
            "badge": "MÉTODO FEYNMAN"
        },
        "parcial": {
            "primary": "#065f46",
            "secondary": "#059669",
            "bg_box": "#ecfdf5",
            "border_box": "#10b981",
            "badge": "MODELO DE PARCIAL / ACTIVE RECALL"
        }
    }
    t = themes.get(doc_type.lower(), themes["multinivel"])

    body_html = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])

    full_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<style>
@page {{
    size: A4;
    margin: 2.2cm 2cm 2.2cm 2cm;
}}
body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #1f2937;
    line-height: 1.65;
    font-size: 11pt;
}}
.header-badge {{
    display: inline-block;
    background-color: {t['primary']};
    color: white;
    font-weight: bold;
    font-size: 8.5pt;
    padding: 3px 9px;
    border-radius: 4px;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
    text-transform: uppercase;
}}
h1 {{
    color: {t['primary']};
    font-size: 20pt;
    border-bottom: 2px solid {t['secondary']};
    padding-bottom: 6px;
    margin-top: 5px;
    margin-bottom: 16px;
}}
h2 {{
    color: {t['primary']};
    font-size: 14pt;
    margin-top: 22px;
    margin-bottom: 8px;
    border-bottom: 1px solid #e5e7eb;
    padding-bottom: 4px;
}}
h3 {{
    color: {t['secondary']};
    font-size: 12pt;
    margin-top: 16px;
    margin-bottom: 6px;
}}
p, li {{
    color: #374151;
    text-align: justify;
}}
ul, ol {{
    padding-left: 20px;
    margin-top: 6px;
    margin-bottom: 12px;
}}
li {{
    margin-bottom: 4px;
}}
blockquote {{
    background-color: {t['bg_box']};
    border-left: 4px solid {t['border_box']};
    margin: 14px 0;
    padding: 10px 14px;
    border-radius: 0 4px 4px 0;
    color: #1f2937;
}}
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 10pt;
}}
th, td {{
    border: 1px solid #d1d5db;
    padding: 7px 10px;
    text-align: left;
}}
th {{
    background-color: {t['bg_box']};
    color: {t['primary']};
    font-weight: 600;
}}
tr:nth-child(even) {{
    background-color: #f9fafb;
}}
code {{
    background: #f3f4f6;
    padding: 2px 5px;
    border-radius: 3px;
    font-size: 9.5pt;
}}
</style>
</head>
<body>
<div class="header-badge">{t['badge']}</div>
{body_html}
</body>
</html>
"""

    temp_html = md_path + ".temp.html"
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(full_html)

    out_dir = os.path.dirname(os.path.abspath(pdf_path)) or "."
    profile_dir = "/tmp/lo_profile"
    cmd = [
        "libreoffice",
        f"-env:UserInstallation=file://{profile_dir}",
        "--headless",
        "--convert-to", "pdf:writer_pdf_Export",
        temp_html,
        "--outdir", out_dir
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    
    generated_pdf = temp_html.replace(".temp.html", ".temp.pdf")
    if os.path.exists(temp_html):
        os.remove(temp_html)
        
    if os.path.exists(generated_pdf):
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
        os.rename(generated_pdf, pdf_path)
        print(f"PDF generado exitosamente: {pdf_path}")
        return True
    else:
        print(f"Error generando PDF: {res.stderr}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 generar_pdf.py <archivo.md> <salida.pdf> [multinivel|feynman|parcial]")
        sys.exit(1)
    doc_type = sys.argv[3] if len(sys.argv) > 3 else "multinivel"
    success = md_to_pdf(sys.argv[1], sys.argv[2], doc_type)
    sys.exit(0 if success else 1)
