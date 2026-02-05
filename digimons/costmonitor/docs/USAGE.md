# Guia de Uso - costmonitor

## Tutorial Paso a Paso

Este tutorial muestra como usar **CostMonitor** para costos.

### 1) Instalacion rapida

```bash
pip install -e .
```

### 2) Importacion e inicializacion

```python
from costmonitor.core import CostMonitor

digimon = CostMonitor()
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
if not digimon.validate(cost_data):
    raise ValueError("Datos invalidos")
```

### 5) Ejecutar el analisis

```python
result = digimon.analyze(cost_data=cost_data)
print(result.status)
print(result.message)
```

---

Ver tambien: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)
