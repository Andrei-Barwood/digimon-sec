# Guia de Uso - geodesic_ledger

## Tutorial Paso a Paso

Este tutorial muestra como usar **GeodesicLedger** para costos.

### 1) Instalacion rapida

```bash
pip install -e .
```

### 2) Importacion e inicializacion

```python
from geodesic_ledger.core import GeodesicLedger

modulo = GeodesicLedger()
```

### 3) Preparar los datos de entrada

```python
cost_data = {
    "cost_anomalies": 0,
    "idle_resources": 0,
    "budget_guardrails": True,
}
```

### 4) Validar los datos (opcional)

```python
if not modulo.validate(cost_data):
    raise ValueError("Datos invalidos")
```

### 5) Ejecutar el analisis

```python
result = modulo.analyze(cost_data=cost_data)
print(result.status)
print(result.message)
```

---

Ver tambien: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)
