# API Reference - lemniscate_archive

## Class: LemniscateArchive

### Constructor

```python
LemniscateArchive(config: Optional[Dict[str, Any]] = None)
```

**Parametros de Configuracion:**

- `strict_mode`: Si True, falla ante settings criticos faltantes
- `min_retention_days`: Dias minimos de retencion
- `max_backup_age_hours`: Maximo de horas desde el ultimo backup
- `require_cross_region`: Requerir replicacion cross-region
- `severity_threshold`: Severidad minima a reportar

### Metodos Principales

#### `audit_backups(backup_data)`

Audita backups y retorna un `AuditReport`.

#### `analyze(backup_data)`

Ejecuta el analisis principal y retorna un `AnalysisResult`.

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Retorna metadata del módulo.

---

Ver tambien: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
