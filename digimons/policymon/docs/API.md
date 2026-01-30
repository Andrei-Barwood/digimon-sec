# API Reference - policymon

## Class: Policymon

### Constructor

```python
Policymon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- No hay parámetros de configuración específicos documentados.

### Métodos Principales

#### `check_policy(policy_name, data)`

Verifica una política específica.

Args:
    policy_name: Nombre de la política
    data: Datos a verificar

Returns:
    PolicyCheck con resultados

#### `audit_policies(checks)`

Audita múltiples políticas.

Args:
    checks: Lista de verificaciones de política

Returns:
    PolicyAudit con resultados

#### `analyze(policy_check, policy_checks)`

Ejecuta verificación: una política o múltiples.

Args:
    policy_check: Verificación individual
    policy_checks: Lista de verificaciones

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for policymon

**Campos:**
- `name`
- `strict_mode`
- `check_permissions`
- `check_encryption`
- `debug`

### PolicyCheck

Result of a policy check

**Campos:**
- `policy_name`
- `compliant`
- `violations`
- `warnings`
- `recommendations`

### PolicyAudit

Result of policy audit

**Campos:**
- `total_checks`
- `passed_checks`
- `failed_checks`
- `checks`
- `audit_summary`

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
