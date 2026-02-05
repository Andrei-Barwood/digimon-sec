# API Reference - dockermon

## Class: Dockermon

### Constructor

```python
Dockermon(config: Optional[Dict[str, Any]] = None)
```

**Parametros de Configuracion:**

- `strict_mode`: Si True, falla ante settings criticos faltantes
- `require_signed_images`: Requerir imagenes firmadas
- `require_read_only_fs`: Requerir filesystem read-only
- `severity_threshold`: Severidad minima a reportar

### Metodos Principales

#### `audit_container(container_data)`

Audita contenedor y retorna un `AuditReport`.

#### `analyze(container_data)`

Ejecuta el analisis principal y retorna un `AnalysisResult`.

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Retorna metadata del Digimon.

---

Ver tambien: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
