# Guia de Uso - cloudsecmon

## Tutorial Paso a Paso

Este tutorial muestra como auditar configuraciones cloud con **CloudSecmon**.

### 1) Instalacion rapida

```bash
pip install -e .
```

### 2) Importacion e inicializacion

```python
from cloudsecmon.core import CloudSecmon

digimon = CloudSecmon()
```

### 3) Preparar los datos de entrada

```python
config_data = {
    "encryption_enabled": True,
    "logging_enabled": True,
    "mfa_enabled": True,
    "public_access": False,
}
```

### 4) Validar los datos (opcional)

```python
if not digimon.validate(config_data):
    raise ValueError("Config data invalida")
```

### 5) Ejecutar el analisis

```python
result = digimon.analyze(config_data=config_data)
print(result.status)
print(result.message)
```

### 6) Interpretar resultados

```python
if result.status == "success":
    print("Todo OK")
elif result.status == "warning":
    print("Se detectaron hallazgos")
else:
    print("Error en el analisis")
```

### 7) Ajustar configuracion avanzada

```python
digimon = CloudSecmon(config={
    "strict_mode": True,
    "severity_threshold": "medium",
    "require_encryption": True,
    "require_logging": True,
    "require_mfa": True,
})
```

---

Ver tambien: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)

