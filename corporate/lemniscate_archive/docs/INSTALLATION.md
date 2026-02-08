# Guia de Instalacion - lemniscate_archive

## Requisitos Previos

- Python 3.10+
- pip o poetry
- Git

## Instalacion desde PyPI

```bash
pip install lemniscate_archive
```

## Instalacion desde Codigo Fuente

```bash
git clone https://github.com/snocomm-security/snocomm-security-suite.git
cd snocomm-security-suite/corporate/lemniscate_archive
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

## Verificacion de Instalacion

```python
from lemniscate_archive.core import LemniscateArchive

modulo = LemniscateArchive()
print(modulo.get_info())
```

---

Ver tambien: [USAGE.md](USAGE.md), [API.md](API.md), [ARCHITECTURE.md](ARCHITECTURE.md)
