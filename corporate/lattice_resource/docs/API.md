# API Reference - lattice_resource

## Class: LatticeResource

### Constructor

```python
LatticeResource(config: Optional[Dict[str, Any]] = None)
```

**Parametros de Configuracion:**

- `strict_mode`: Si True, falla ante settings criticos faltantes
- `max_cpu_percent`: Maximo de CPU permitido
- `max_memory_percent`: Maximo de memoria permitida
- `max_storage_percent`: Maximo de storage permitido
- `severity_threshold`: Severidad minima a reportar

### Metodos Principales

#### `audit_usage(usage_data)`

Audita uso de recursos y retorna un `AuditReport`.

#### `analyze(usage_data)`

Ejecuta el analisis principal y retorna un `AnalysisResult`.

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Retorna metadata del módulo.

---

Ver tambien: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
