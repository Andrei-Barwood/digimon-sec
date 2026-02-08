# Guia de Instalacion - simplex_container

## Requisitos Previos

- Python 3.10+
- pip o poetry
- Git

## Instalacion desde PyPI

```bash
pip install simplex_container
```

## Instalacion desde Codigo Fuente

```bash
git clone https://github.com/snocomm-security/snocomm-security-suite.git
cd snocomm-security-suite/corporate/simplex_container
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

## Verificacion de Instalacion

```python
from simplex_container.core import SimplexContainer

modulo = SimplexContainer()
print(modulo.get_info())
```

---

Ver tambien: [USAGE.md](USAGE.md), [API.md](API.md), [ARCHITECTURE.md](ARCHITECTURE.md)
