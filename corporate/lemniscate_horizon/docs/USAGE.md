# Guia de Uso - lemniscate_horizon

## Tutorial Paso a Paso

Este tutorial muestra como usar **LemniscateHorizon** para cumplimiento.

### 1) Instalacion rapida

```bash
pip install -e .
```

### 2) Importacion e inicializacion

```python
from lemniscate_horizon.core import LemniscateHorizon

modulo = LemniscateHorizon()
```

### 3) Preparar los datos de entrada

```python
compliance_data = {
    "passed_controls": 3,
    "evidence_collected": True,
    "continuous_monitoring": True,
    "frameworks_checked": ["SOC2"],
}
```

### 4) Validar los datos (opcional)

```python
if not modulo.validate(compliance_data):
    raise ValueError("Datos invalidos")
```

### 5) Ejecutar el analisis

```python
result = modulo.analyze(compliance_data=compliance_data)
print(result.status)
print(result.message)
```

---

Ver tambien: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)
