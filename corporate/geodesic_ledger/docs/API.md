# API Reference - geodesic_ledger

## Class: GeodesicLedger

### Constructor

```python
GeodesicLedger(config: Optional[Dict[str, Any]] = None)
```

**Parametros de Configuracion:**

- `strict_mode`: Si True, falla ante settings criticos faltantes
- `max_idle_resources`: Maximo de recursos ociosos
- `max_cost_anomalies`: Maximo de anomalias permitidas
- `require_budget_guardrails`: Requerir guardrails de presupuesto
- `severity_threshold`: Severidad minima a reportar

### Metodos Principales

#### `audit_costs(cost_data)`

Audita costos y retorna un `AuditReport`.

#### `analyze(cost_data)`

Ejecuta el analisis principal y retorna un `AnalysisResult`.

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Retorna metadata del módulo.

---

Ver tambien: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
