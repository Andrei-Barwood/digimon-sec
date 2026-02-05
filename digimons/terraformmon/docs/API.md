# API Reference - terraformmon

## Class: Terraformmon

### Constructor

```python
Terraformmon(config: Optional[Dict[str, Any]] = None)
```

**Parametros de Configuracion:**

- `strict_mode`: Si True, falla ante settings criticos faltantes
- `require_remote_state_encrypted`: Requerir cifrado del state
- `require_plan_approval`: Requerir aprobacion del plan
- `require_modules_pinned`: Requerir versiones fijadas
- `severity_threshold`: Severidad minima a reportar

### Metodos Principales

#### `validate_iac(iac_data)`

Audita IaC y retorna un `AuditReport`.

#### `analyze(iac_data)`

Ejecuta el analisis principal y retorna un `AnalysisResult`.

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Retorna metadata del Digimon.

---

Ver tambien: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
