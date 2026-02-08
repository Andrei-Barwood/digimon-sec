# API Reference - lemniscate_horizon

## Class: LemniscateHorizon

### Constructor

```python
LemniscateHorizon(config: Optional[Dict[str, Any]] = None)
```

**Parametros de Configuracion:**

- `strict_mode`: Si True, falla ante settings criticos faltantes
- `min_passed_controls`: Controles minimos aprobados
- `require_evidence`: Requerir evidencia de cumplimiento
- `require_continuous_monitoring`: Requerir monitoreo continuo
- `severity_threshold`: Severidad minima a reportar

### Metodos Principales

#### `audit_compliance(compliance_data)`

Audita cumplimiento y retorna un `AuditReport`.

#### `analyze(compliance_data)`

Ejecuta el analisis principal y retorna un `AnalysisResult`.

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Retorna metadata del módulo.

---

Ver tambien: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
