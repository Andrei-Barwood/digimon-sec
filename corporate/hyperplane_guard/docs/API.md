# API Reference - hyperplane_guard

## Class: HyperplaneGuard

### Constructor

```python
HyperplaneGuard(config: Optional[Dict[str, Any]] = None)
```

**Parametros de Configuracion:**

- `strict_mode`: Si True, falla ante settings criticos faltantes
- `allowed_ports`: Lista de puertos permitidos
- `require_logging`: Requerir logging de firewall
- `severity_threshold`: Severidad minima a reportar

### Metodos Principales

#### `audit_rules(rules_data)`

Audita reglas de firewall y retorna un `AuditReport`.

#### `analyze(rules_data)`

Ejecuta el analisis principal y retorna un `AnalysisResult`.

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Retorna metadata del módulo.

---

Ver tambien: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)

