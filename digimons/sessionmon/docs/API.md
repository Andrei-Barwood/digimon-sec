# API Reference - sessionmon

## Class: Sessionmon

### Constructor

```python
Sessionmon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- No hay parámetros de configuración específicos documentados.

### Métodos Principales

#### `create_session(user_id, ip_address, user_agent)`

Crea una nueva sesión.

Args:
    user_id: ID del usuario
    ip_address: Dirección IP (opcional)
    user_agent: User agent (opcional)

Returns:
    Session creada

#### `validate_session(session_id)`

Valida una sesión.

Args:
    session_id: ID de la sesión

Returns:
    True si la sesión es válida

#### `analyze_sessions()`

Analiza todas las sesiones activas.

Returns:
    SessionAnalysis con resultados

#### `analyze(action, user_id)`

Ejecuta análisis: analizar sesiones o crear sesión.

Args:
    action: Acción ("analyze" o "create")
    user_id: ID de usuario (si action="create")

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for sessionmon

**Campos:**
- `name`
- `session_timeout`
- `max_concurrent_sessions`
- `enable_session_fixation`
- `debug`

### Session

Session information

**Campos:**
- `session_id`
- `user_id`
- `created_at`
- `expires_at`
- `last_activity`
- `ip_address`
- `user_agent`

### SessionAnalysis

Result of session analysis

**Campos:**
- `total_sessions`
- `active_sessions`
- `expired_sessions`
- `sessions_by_user`
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
- `session_timeout`
- `max_concurrent_sessions`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
