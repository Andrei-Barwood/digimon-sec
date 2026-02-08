# Guía para contribuir

Gracias por tu interés en contribuir al **Snocomm Security Suite**. Este documento describe cómo configurar el entorno y ejecutar los tests, y cómo añadir o modificar módulos (empresas filiales).

---

## Cómo clonar y ejecutar tests

1. Clona el repositorio:
   ```bash
   git clone https://github.com/snocomm-security/snocomm-security-suite.git
   cd snocomm-security-suite
   ```

2. Crea un entorno virtual (recomendado) e instala dependencias mínimas para ejecutar tests:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # En Windows: .venv\Scripts\activate
   pip install pytest pytest-cov pydantic
   ```

3. Ejecuta todos los tests de los módulos corporativos:
   ```bash
   ./tools/test_all_modules.sh
   ```
   o, con el runner en Python:
   ```bash
   python tools/test_all_modules.py
   python tools/test_all_modules.py --quiet    # solo resumen
   python tools/test_all_modules.py --verbose  # salida detallada
   ```

4. Ejecuta los tests de integración del pipeline:
   ```bash
   pytest tests/test_integration.py -v
   ```

---

## Naming Guide y registro de empresas

- El **Naming Guide** (convención de nombres: geometría + minimalismo/futurismo) está en el [README principal](README.md#naming-guide).
- La fuente de verdad de empresas, dominios y nombres técnicos es [corporate/manifest.yaml](corporate/manifest.yaml). Cualquier nueva empresa o cambio de identidad debe reflejarse ahí con: `folder_name`, `package_name`, `class_name`, `display_name`, `domain`.

---

## Estructura esperada de un módulo

Cada empresa/módulo bajo `corporate/` debe seguir esta estructura:

```
corporate/<folder_name>/
├── docs/
│   ├── API.md
│   ├── ARCHITECTURE.md
│   ├── INSTALLATION.md
│   ├── PRESENTACION_CORPORATIVA.md
│   └── USAGE.md
├── examples/
│   ├── basic_usage.py
│   └── README.md
├── src/<package_name>/
│   ├── __init__.py
│   ├── core.py
│   ├── models.py
│   └── (opcional) utils.py
├── tests/
│   ├── conftest.py
│   └── test_core.py
├── pyproject.toml
├── LICENSE
└── README.md
```

- `folder_name` y `package_name` suelen coincidir (snake_case).
- La clase principal en `core.py` debe usar PascalCase (ej. `TesseractCovenant`).
- Los scripts en `tools/` (p. ej. `generate_docs.py`, `generate_presentaciones_corporativas.py`) usan el manifest para generar documentación; al añadir un módulo, regístralo en el manifest y regenera si aplica.

---

## Añadir un nuevo módulo

1. Elige un nombre según el [Naming Guide](README.md#naming-guide) y un dominio (ej. `compliance`, `iam`, `threat-intel`).
2. Añade una entrada en [corporate/manifest.yaml](corporate/manifest.yaml) con `folder_name`, `package_name`, `class_name`, `display_name`, `domain`. Si el módulo reemplaza uno legacy, puedes usar `legacy_folder` como referencia histórica.
3. Crea la carpeta `corporate/<folder_name>/` y copia la estructura de un módulo existente (p. ej. `tesseract_covenant` o `helix_filter`).
4. Implementa `core.py`, `models.py`, docs y tests. Asegura que `get_info()` devuelva `"status": "Production"` y que los tests pasen.
5. Opcional: ejecuta `python tools/generate_docs.py` y `python tools/generate_presentaciones_corporativas.py` si usas plantillas compartidas para documentación y presentaciones.

---

*Snocomm Security Suite — Contribuciones bienvenidas.*
