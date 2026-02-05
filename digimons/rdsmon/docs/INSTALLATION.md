# Guia de Instalacion - rdsmon

## Requisitos Previos

- Python 3.10+
- pip o poetry
- Git

## Instalacion desde PyPI

```bash
pip install rdsmon
```

## Instalacion desde Codigo Fuente

```bash
git clone https://github.com/yourusername/digimon-sec-suite.git
cd digimon-sec-suite/digimons/rdsmon
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

## Verificacion de Instalacion

```python
from rdsmon.core import RDSmon

digimon = RDSmon()
print(digimon.get_info())
```

---

Ver tambien: [USAGE.md](USAGE.md), [API.md](API.md), [ARCHITECTURE.md](ARCHITECTURE.md)
