# Guia de Instalacion - compliancecloud

## Requisitos Previos

- Python 3.10+
- pip o poetry
- Git

## Instalacion desde PyPI

```bash
pip install compliancecloud
```

## Instalacion desde Codigo Fuente

```bash
git clone https://github.com/yourusername/digimon-sec-suite.git
cd digimon-sec-suite/digimons/compliancecloud
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

## Verificacion de Instalacion

```python
from compliancecloud.core import ComplianceCloud

digimon = ComplianceCloud()
print(digimon.get_info())
```

---

Ver tambien: [USAGE.md](USAGE.md), [API.md](API.md), [ARCHITECTURE.md](ARCHITECTURE.md)
