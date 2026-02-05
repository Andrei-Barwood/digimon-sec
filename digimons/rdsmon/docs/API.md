# API Reference - rdsmon

## Class: RDSmon

### Constructor

```python
RDSmon(config: Optional[Dict[str, Any]] = None)
```

**Parametros de Configuracion:**

- `strict_mode`: Si True, falla ante settings criticos faltantes
- `min_backup_retention_days`: Minimo de dias de retencion
- `require_encryption`: Requerir cifrado en storage
- `require_multi_az`: Requerir despliegue Multi-AZ
- `severity_threshold`: Severidad minima a reportar

### Metodos Principales

#### `audit_database(db_data)`

Audita base de datos y retorna un `AuditReport`.

#### `analyze(db_data)`

Ejecuta el analisis principal y retorna un `AnalysisResult`.

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Retorna metadata del Digimon.

---

Ver tambien: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
