# API Reference - gdprmon

## Class: GDPRmon

### Constructor

```python
GDPRmon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- No hay parámetros de configuración específicos documentados.

### Métodos Principales

#### `audit_compliance(target_data)`

Audita cumplimiento GDPR de un objetivo.

Args:
    target_data: Datos del objetivo a auditar

Returns:
    GDPRComplianceReport con resultados

#### `analyze(target_data)`

Ejecuta análisis: auditoría GDPR.

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

Configuration model for gdprmon

**Campos:**
- `name`
- `strict_mode`
- `check_data_subject_rights`
- `check_data_breach_notification`
- `check_consent_management`
- `debug`

### GDPRCheck

Individual GDPR compliance check result

**Campos:**
- `check_id`
- `article`
- `requirement`
- `status`
- `severity`
- `description`
- `remediation`
- `evidence`

### GDPRComplianceReport

GDPR compliance report

**Campos:**
- `report_id`
- `total_checks`
- `passed_checks`
- `failed_checks`
- `warning_checks`
- `compliance_score`
- `checks`
- `data_subject_rights_status`
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
