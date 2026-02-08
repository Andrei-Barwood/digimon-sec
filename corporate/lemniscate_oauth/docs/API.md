# API Reference - lemniscate_oauth

## Class: LemniscateOauth

### Constructor

```python
LemniscateOauth(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `supported_flows`: Configura supported_flows (Default: `["authorization_code", "client_credentials", "implicit"]`)

### Métodos Principales

#### `generate_token(flow_type, scope, expires_in)`

Genera un token OAuth.

Args:
    flow_type: Tipo de flujo OAuth
    scope: Scope del token (opcional)
    expires_in: Expiración en segundos (default: 3600)

Returns:
    OAuthToken generado

#### `validate_token(access_token)`

Valida un token OAuth.

Args:
    access_token: Token a validar

Returns:
    True si el token es válido

#### `analyze_oauth()`

Analiza todos los tokens OAuth.

Returns:
    OAuthAnalysis con resultados

#### `analyze(action, token_data)`

Ejecuta análisis: analizar OAuth o generar token.

Args:
    action: Acción ("analyze" o "generate")
    token_data: Datos de token (si action="generate")

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del módulo.



## Modelos de Datos

### ModuleConfig

Configuration model for lemniscate_oauth

**Campos:**
- `name`
- `authorization_url`
- `token_url`
- `client_id`
- `supported_flows`
- `debug`

### OAuthToken

OAuth token information

**Campos:**
- `access_token`
- `token_type`
- `expires_in`
- `refresh_token`
- `scope`
- `created_at`

### OAuthAnalysis

Result of OAuth analysis

**Campos:**
- `total_tokens`
- `active_tokens`
- `tokens_by_flow`
- `expired_tokens`
- `violations`
- `analysis_summary`

### AnalysisResult

Result model for analysis operations

**Campos:**
- `status`
- `message`
- `data`
- `errors`

### ModuleInfo

Information model for módulo metadata

**Campos:**
- `name`
- `mission`
- `role`
- `status`
- `supported_flows`
- `client_id`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
