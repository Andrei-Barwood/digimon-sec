# Guia de Uso - compliancecloud

## Tutorial Paso a Paso

Este tutorial muestra como usar **ComplianceCloud** para cumplimiento.

### 1) Instalacion rapida

```bash
pip install -e .
```

### 2) Importacion e inicializacion

```python
from compliancecloud.core import ComplianceCloud

digimon = ComplianceCloud()
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
if not digimon.validate(compliance_data):
    raise ValueError("Datos invalidos")
```

### 5) Ejecutar el analisis

```python
result = digimon.analyze(compliance_data=compliance_data)
print(result.status)
print(result.message)
```

---

Ver tambien: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)
