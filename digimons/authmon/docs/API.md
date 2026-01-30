# API Reference - authmon

## Class: Authmon

### Constructor

```python
Authmon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `auth_methods`: Configura auth_methods (Default: `["password", "mfa", "biometric"]`)

### Métodos Principales

#### `authenticate(user_id, credentials, method)`

Autentica un usuario.

Args:
    user_id: ID del usuario
    credentials: Credenciales (password, token, etc.)
    method: Método de autenticación

Returns:
    AuthResult con resultado de autenticación

#### `analyze(user_id, credentials, method)`

Ejecuta análisis de autenticación.

Args:
    user_id: ID del usuario
    credentials: Credenciales
    method: Método de autenticación (opcional)

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for authmon

**Campos:**
- `name`
- `auth_methods`
- `max_attempts`
- `lockout_duration`
- `debug`

### AuthResult

Result of authentication attempt

**Campos:**
- `success`
- `user_id`
- `method`
- `timestamp`
- `attempts_remaining`
- `locked`
- `errors`

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
- `auth_methods`
- `max_attempts`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
