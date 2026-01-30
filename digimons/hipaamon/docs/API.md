# API Reference - hipaamon

## Class: HIPAAmon

### Constructor

```python
HIPAAmon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- No hay parámetros de configuración específicos documentados.

### Métodos Principales

#### `audit_compliance(target_data)`

Audita cumplimiento HIPAA de un objetivo.

Args:
    target_data: Datos del objetivo a auditar

Returns:
    HIPAAComplianceReport con resultados

#### `analyze(target_data)`

Ejecuta análisis: auditoría HIPAA.

Args:
    target_data: Datos del objetivo a auditar

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for hipaamon

**Campos:**
- `name`
- `strict_mode`
- `check_phi_protection`
- `check_access_controls`
- `check_audit_logs`
- `debug`

### HIPAACheck

Individual HIPAA compliance check result

**Campos:**
- `check_id`
- `section`
- `requirement`
- `status`
- `severity`
- `description`
- `remediation`
- `evidence`

### HIPAAComplianceReport

HIPAA compliance report

**Campos:**
- `report_id`
- `total_checks`
- `passed_checks`
- `failed_checks`
- `warning_checks`
- `compliance_score`
- `checks`
- `phi_protection_status`
- `summary`

### AnalysisResult

Result model for analysis operations

**Campos:**
- `status`
- `message`
- `data`
- `errors`

### DigimonInfo

Information model for Digimon metadata

**Campos:**
- `name`
- `mission`
- `role`
- `status`
- `strict_mode`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
