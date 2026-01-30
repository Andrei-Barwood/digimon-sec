# API Reference - identitymon

## Class: Identitymon

### Constructor

```python
Identitymon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- No hay parámetros de configuración específicos documentados.

### Métodos Principales

#### `validate_identity(identity_data)`

Valida y crea una identidad.

Args:
    identity_data: Datos de la identidad

Returns:
    Identity validada

#### `analyze_identities(identities)`

Analiza múltiples identidades.

Args:
    identities: Lista de identidades

Returns:
    IdentityAnalysis con resultados

#### `analyze(identity, identities)`

Ejecuta análisis: una identidad o múltiples.

Args:
    identity: Identidad individual
    identities: Lista de identidades

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for identitymon

**Campos:**
- `name`
- `validate_attributes`
- `check_roles`
- `enforce_policies`
- `debug`

### Identity

Identity information

**Campos:**
- `user_id`
- `username`
- `email`
- `roles`
- `attributes`
- `status`

### IdentityAnalysis

Result of identity analysis

**Campos:**
- `total_identities`
- `active_identities`
- `inactive_identities`
- `roles_distribution`
- `policy_violations`
- `analysis_summary`

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
- `validate_attributes`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
