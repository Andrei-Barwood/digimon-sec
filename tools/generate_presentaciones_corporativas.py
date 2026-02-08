#!/usr/bin/env python3
"""
Genera PRESENTACION_CORPORATIVA.md para cada módulo Snocomm.
Lee corporate/manifest.yaml y tools/corporate_presentation_content.yaml.
Requiere: PyYAML (pip install pyyaml) o contenido embebido.
"""
from pathlib import Path
import re

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


def parse_manifest(manifest_path: Path) -> list:
    out = []
    cur = None
    for line in manifest_path.read_text().splitlines():
        line = line.rstrip()
        if line.startswith("  - legacy_folder:"):
            if cur:
                out.append(cur)
            cur = {"legacy_folder": line.split(":", 1)[1].strip()}
        elif cur and line.startswith("    ") and ":" in line:
            k, _, v = line.strip().partition(":")
            if k and v.strip():
                cur[k] = v.strip()
    if cur:
        out.append(cur)
    return out


def load_content_yaml(path: Path) -> dict:
    if not HAS_YAML:
        raise SystemExit("Instale PyYAML: pip install pyyaml")
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data or {}


def build_md(display_name: str, domain: str, c: dict) -> str:
    if not c:
        c = {
            "titulo_rubro": domain.replace("-", " ").title(),
            "descripcion": "Soluciones profesionales de ciberseguridad para su organización.",
            "con_vs_sin_rows": [],
            "beneficios": "Reducción de riesgos y cumplimiento normativo.",
            "ejemplo_vida": "Casos de éxito en el sector.",
            "ganancia_invertir": "ROI positivo con personal capacitado.",
            "perdida_no_invertir": "Riesgos operativos y legales.",
            "diferenciador": "Experiencia y enfoque Snocomm.",
        }
    rows = c.get("con_vs_sin_rows") or []
    table_body = "\n".join(
        "| " + " | ".join(r) + " |" for r in rows
    )
    table = (
        "| Aspecto | Con " + display_name + " | Sin solución adecuada |\n"
        "|---------|----------------------|--------------------------|\n"
        + table_body
    ) if rows else "*(Consulte con nuestro equipo para una comparativa detallada.)*"

    return f"""# {display_name} — Presentación corporativa

## {c.get('titulo_rubro', domain)} | Snocomm Security Suite

**Documento para el comprador** — Confidencial

---

### Introducción

{c.get('descripcion', '')}

Este documento resume los beneficios de adoptar **{display_name}**, los resultados de invertir en personal capacitado para gestionarlo y los riesgos de no hacerlo, con ejemplos que ilustran tanto el impacto técnico como el humano en su organización.

---

### Con {display_name} vs sin solución adecuada

{table}

---

### Beneficios concretos

{c.get('beneficios', '')}

---

### Ejemplo de impacto real (lado técnico y humano)

{c.get('ejemplo_vida', '')}

---

### Ganancia de utilizar el producto e invertir en personal capacitado

{c.get('ganancia_invertir', '')}

| Inversión | Retorno esperado |
|-----------|------------------|
| Producto + 1 persona dedicada (o parte del tiempo) | Reducción de incidentes, multas evitadas, auditorías aprobadas, ventaja competitiva |
| Formación continua | Equipo alineado con mejores prácticas y normativa actual |

---

### Pérdidas de no invertir en personal humano capacitado

{c.get('perdida_no_invertir', '')}

| Riesgo | Impacto típico |
|--------|-----------------|
| Sin dueño del producto | Controles desactualizados, nadie responde ante auditoría o incidente |
| Sin formación | Errores de configuración, falsa sensación de seguridad |
| Sin tiempo dedicado | Parches de emergencia, costes ocultos, burnout del equipo |

---

### Por qué elegirnos

{c.get('diferenciador', '')}

**Snocomm** agrupa empresas especializadas por ámbito. Al contratar **{display_name}**, usted obtiene un área de trabajo dedicada a **{c.get('titulo_rubro', domain)}**, con producto, documentación y soporte alineados con estándares actuales del sector.

---

### Próximos pasos

1. Contacte a Snocomm para una demostración adaptada a su sector.
2. Solicite una evaluación de brechas (gap) sin compromiso.
3. Defina el perfil de la persona que gestionará el producto en su organización.

---

*Documento generado por Snocomm Security Suite. Versión para comprador.*
"""


def main():
    root = Path(__file__).resolve().parents[1]
    manifest_path = root / "corporate" / "manifest.yaml"
    content_path = root / "tools" / "corporate_presentation_content.yaml"

    modules = parse_manifest(manifest_path)
    content_by_domain = load_content_yaml(content_path)

    for m in modules:
        folder = m["folder_name"]
        display_name = m["display_name"]
        domain = m["domain"]
        c = content_by_domain.get(domain, {})
        md = build_md(display_name, domain, c)
        out_file = root / "corporate" / folder / "docs" / "PRESENTACION_CORPORATIVA.md"
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(md, encoding="utf-8")
        print(f"  OK: {folder}/docs/PRESENTACION_CORPORATIVA.md")


if __name__ == "__main__":
    main()
