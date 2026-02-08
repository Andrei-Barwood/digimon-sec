# Guía de Instalación - lattice_permission

## Requisitos Previos

- Python 3.10+
- pip o poetry
- Git

## Instalación desde PyPI

```bash
pip install lattice_permission
```

## Instalación desde Código Fuente

```bash
git clone https://github.com/snocomm-security/snocomm-security-suite.git
cd snocomm-security-suite/corporate/lattice_permission
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

## Verificación de Instalación

```python
from lattice_permission.core import LatticePermission

modulo = LatticePermission()
print(modulo.get_info())
```

---

Ver también: [PRESENTACION_CORPORATIVA.md](PRESENTACION_CORPORATIVA.md) (documento para comprador), [USAGE.md](USAGE.md), [API.md](API.md), [ARCHITECTURE.md](ARCHITECTURE.md)
