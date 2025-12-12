# Guía de Uso - Mnemomon (Mega)

## Inicio Rápido

### Instalación

```bash
pip install -e .
```

### Uso Básico

```python
from mnemomon.core import Mnemomon

digimon = Mnemomon()

# Verificación puntual con checksum esperado
result = digimon.analyze(
    backup_path="/path/to/backup.tar.gz",
    expected_checksum="abc123..."
)
print(result)
```

## Auditoría de carpeta completa

```python
from mnemomon.core import mnemomon

digimon = Mnemomon(config={"min_retention_days": 30})

audit = digimon.analyze(directory_path="/backups/daily")
print(audit)
```

---

Ver también: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)
