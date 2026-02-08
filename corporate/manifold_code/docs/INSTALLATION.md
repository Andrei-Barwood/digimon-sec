# Guia de Instalacion - manifold_code

## Requisitos Previos

- Python 3.10+
- pip o poetry
- Git

## Instalacion desde PyPI

```bash
pip install manifold_code
```

## Instalacion desde Codigo Fuente

```bash
git clone https://github.com/snocomm-security/snocomm-security-suite.git
cd snocomm-security-suite/corporate/manifold_code
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

## Verificacion de Instalacion

```python
from manifold_code.core import ManifoldCode

modulo = ManifoldCode()
print(modulo.get_info())
```

---

Ver tambien: [USAGE.md](USAGE.md), [API.md](API.md), [ARCHITECTURE.md](ARCHITECTURE.md)
