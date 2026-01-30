# API Reference - privacymon

## Class: Privacymon

### Constructor

```python
Privacymon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- No hay parámetros de configuración específicos documentados.

### Métodos Principales

#### `audit_policy(target_data)`

Audita política de privacidad de un objetivo.

Args:
    target_data: Datos del objetivo a auditar

Returns:
    PrivacyAudit con resultados

#### `analyze(target_data)`

Ejecuta análisis: auditoría de privacidad.

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

Configuration model for privacymon

**Campos:**
- `name`
- `strict_mode`
- `check_data_collection`
- `check_data_sharing`
- `check_user_rights`
- `debug`

### PrivacyCheck

Individual privacy policy check result

**Campos:**
- `check_id`
- `policy_area`
- `requirement`
- `status`
- `severity`
- `description`
- `remediation`
- `evidence`

### PrivacyAudit

Privacy policy audit result

**Campos:**
- `audit_id`
- `total_checks`
- `passed_checks`
- `failed_checks`
- `warning_checks`
- `compliance_score`
- `checks`
- `privacy_policy_status`
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
