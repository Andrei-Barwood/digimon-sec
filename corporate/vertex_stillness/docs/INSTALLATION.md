# Guia de Instalacion - vertex_stillness

## Requisitos Previos

- Python 3.10+
- pip o poetry
- Git

## Instalacion desde PyPI

```bash
pip install vertex_stillness
```

## Instalacion desde Codigo Fuente

```bash
git clone https://github.com/snocomm-security/snocomm-security-suite.git
cd snocomm-security-suite/corporate/vertex_stillness
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

## Verificacion de Instalacion

```python
from vertex_stillness.core import VertexStillness

modulo = VertexStillness()
print(modulo.get_info())
```

---

Ver tambien: [USAGE.md](USAGE.md), [API.md](API.md), [ARCHITECTURE.md](ARCHITECTURE.md)

