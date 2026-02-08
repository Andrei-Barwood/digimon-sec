# API Reference - geodesic_identity

## Class: GeodesicIdentity

### Constructor

```python
GeodesicIdentity(config: Optional[Dict[str, Any]] = None)
```

**Parametros de Configuracion:**

- `strict_mode`: Si True, falla ante settings criticos faltantes
- `severity_threshold`: Severidad minima a reportar
- `require_mfa`: Requerir MFA en usuarios privilegiados
- `require_rotation`: Requerir rotacion de llaves
- `max_inactive_users`: Maximo de usuarios inactivos permitidos

### Metodos Principales

#### `audit_iam(iam_data)`

Audita configuraciones IAM y retorna un `AuditReport`.

#### `analyze(iam_data)`

Ejecuta el analisis principal y retorna un `AnalysisResult`.

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Retorna metadata del módulo.

---

Ver tambien: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)

