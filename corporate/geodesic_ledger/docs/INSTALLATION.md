# Guia de Instalacion - geodesic_ledger

## Requisitos Previos

- Python 3.10+
- pip o poetry
- Git

## Instalacion desde PyPI

```bash
pip install geodesic_ledger
```

## Instalacion desde Codigo Fuente

```bash
git clone https://github.com/snocomm-security/snocomm-security-suite.git
cd snocomm-security-suite/corporate/geodesic_ledger
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

## Verificacion de Instalacion

```python
from geodesic_ledger.core import GeodesicLedger

modulo = GeodesicLedger()
print(modulo.get_info())
```

---

Ver tambien: [USAGE.md](USAGE.md), [API.md](API.md), [ARCHITECTURE.md](ARCHITECTURE.md)
