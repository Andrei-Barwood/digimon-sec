# Guia de Instalacion - kubernetesmon

## Requisitos Previos

- Python 3.10+
- pip o poetry
- Git

## Instalacion desde PyPI

```bash
pip install kubernetesmon
```

## Instalacion desde Codigo Fuente

```bash
git clone https://github.com/yourusername/digimon-sec-suite.git
cd digimon-sec-suite/digimons/kubernetesmon
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

## Verificacion de Instalacion

```python
from kubernetesmon.core import Kubernetesmon

digimon = Kubernetesmon()
print(digimon.get_info())
```

---

Ver tambien: [USAGE.md](USAGE.md), [API.md](API.md), [ARCHITECTURE.md](ARCHITECTURE.md)
