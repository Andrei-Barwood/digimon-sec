# API Reference - ssomon

## Class: SSOmon

### Constructor

```python
SSOmon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- No hay parámetros de configuración específicos documentados.

### Métodos Principales

#### `create_sso_session(user_id, idp, protocol, attributes)`

Crea una sesión SSO.

Args:
    user_id: ID del usuario
    idp: Identity Provider
    protocol: Protocolo (SAML/OIDC)
    attributes: Atributos del usuario (opcional)

Returns:
    SSOSession creada

#### `analyze_sso()`

Analiza las sesiones SSO activas.

Returns:
    SSOAnalysis con resultados

#### `analyze(action, session_data)`

Ejecuta análisis: analizar SSO o crear sesión.

Args:
    action: Acción ("analyze" o "create")
    session_data: Datos de sesión (si action="create")

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for ssomon

**Campos:**
- `name`
- `idp_url`
- `sp_entity_id`
- `enable_saml`
- `enable_oidc`
- `debug`

### SSOSession

SSO session information

**Campos:**
- `session_id`
- `user_id`
- `idp`
- `protocol`
- `created_at`
- `expires_at`
- `attributes`

### SSOAnalysis

Result of SSO analysis

**Campos:**
- `total_sessions`
- `active_sessions`
- `sessions_by_protocol`
- `sessions_by_idp`
- `violations`
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
- `enable_saml`
- `enable_oidc`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
