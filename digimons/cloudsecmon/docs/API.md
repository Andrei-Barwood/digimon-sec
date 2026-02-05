# API Reference - cloudsecmon

## Class: CloudSecmon

### Constructor

```python
CloudSecmon(config: Optional[Dict[str, Any]] = None)
```

**Parametros de Configuracion:**

- `strict_mode`: Si True, falla ante settings criticos faltantes
- `severity_threshold`: Severidad minima a reportar
- `require_encryption`: Requerir cifrado en reposo
- `require_logging`: Requerir logging habilitado
- `require_mfa`: Requerir MFA para administradores

### Metodos Principales

#### `audit_config(config_data)`

Audita configuraciones cloud clave y retorna un `AuditReport`.

#### `analyze(config_data)`

Ejecuta el analisis principal y retorna un `AnalysisResult`.

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Retorna metadata del Digimon.

---

Ver tambien: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)

