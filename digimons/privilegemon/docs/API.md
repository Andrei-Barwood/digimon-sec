# API Reference - privilegemon

## Class: Privilegemon

### Constructor

```python
Privilegemon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- No hay parámetros de configuración específicos documentados.

### Métodos Principales

#### `request_elevation(user_id, requested_privilege, justification)`

Solicita elevación de privilegios.

Args:
    user_id: ID del usuario
    requested_privilege: Nivel de privilegio solicitado
    justification: Justificación (opcional si require_justification=False)

Returns:
    PrivilegeEvent con resultado

#### `audit_privileges()`

Audita todos los eventos de privilegios.

Returns:
    PrivilegeAudit con resultados

#### `analyze(action, elevation_data)`

Ejecuta análisis: auditar o solicitar elevación.

Args:
    action: Acción ("audit" o "request")
    elevation_data: Datos de elevación (si action="request")

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for privilegemon

**Campos:**
- `name`
- `track_elevations`
- `require_justification`
- `max_elevation_duration`
- `debug`

### PrivilegeEvent

Privilege elevation event

**Campos:**
- `event_id`
- `user_id`
- `requested_privilege`
- `justification`
- `granted`
- `timestamp`
- `duration`

### PrivilegeAudit

Result of privilege audit

**Campos:**
- `total_events`
- `granted_count`
- `denied_count`
- `events_by_user`
- `violations`
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
- `require_justification`
- `max_elevation_duration`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
