# Guia de Uso - hyperplane_guard

## Tutorial Paso a Paso

Este tutorial muestra como auditar reglas de firewall con **HyperplaneGuard**.

### 1) Instalacion rapida

```bash
pip install -e .
```

### 2) Importacion e inicializacion

```python
from hyperplane_guard.core import HyperplaneGuard

modulo = HyperplaneGuard()
```

### 3) Preparar los datos de entrada

```python
rules_data = {
    "default_deny": True,
    "open_ports": [80, 443],
    "logging_enabled": True,
}
```

### 4) Validar los datos (opcional)

```python
if not modulo.validate(rules_data):
    raise ValueError("Firewall data invalida")
```

### 5) Ejecutar el analisis

```python
result = modulo.analyze(rules_data=rules_data)
print(result.status)
print(result.message)
```

### 6) Ajustar configuracion avanzada

```python
modulo = HyperplaneGuard(config={
    "allowed_ports": [80, 443],
    "require_logging": True,
    "severity_threshold": "medium",
})
```

---

Ver tambien: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)

