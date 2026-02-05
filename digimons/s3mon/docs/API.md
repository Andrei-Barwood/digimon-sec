# API Reference - s3mon

## Class: S3mon

### Constructor

```python
S3mon(config: Optional[Dict[str, Any]] = None)
```

**Parametros de Configuracion:**

- `strict_mode`: Si True, falla ante settings criticos faltantes
- `require_encryption`: Requerir cifrado en buckets
- `require_versioning`: Requerir versionado
- `require_logging`: Requerir logging de acceso
- `severity_threshold`: Severidad minima a reportar

### Metodos Principales

#### `audit_bucket(bucket_data)`

Audita configuraciones S3 y retorna un `AuditReport`.

#### `analyze(bucket_data)`

Ejecuta el analisis principal y retorna un `AnalysisResult`.

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Retorna metadata del Digimon.

---

Ver tambien: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)

