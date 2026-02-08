# API Reference - helix_incident

## Class: HelixIncident

### Constructor

```python
HelixIncident(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `severity_threshold`: Configura severity_threshold (Default: `"medium"`)

### Métodos Principales

#### `respond_to_incident(incident_type, severity, target, description)`

Responde a un incidente de seguridad.

Args:
    incident_type: Tipo de incidente
    severity: Severidad (critical/high/medium/low)
    target: Objetivo afectado
    description: Descripción opcional

Returns:
    IncidentResponse con acciones tomadas

#### `analyze(incident_type, severity, target, incidents)`

Ejecuta respuesta: un incidente o múltiples.

Args:
    incident_type: Tipo de incidente individual
    severity: Severidad individual
    target: Objetivo individual
    incidents: Lista de incidentes

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del módulo.



## Modelos de Datos

### ModuleConfig

Configuration model for helix_incident

**Campos:**
- `name`
- `auto_contain`
- `severity_threshold`
- `notification_enabled`
- `debug`

### IncidentAction

Incident response action

**Campos:**
- `action_type`
- `target`
- `status`
- `timestamp`

### IncidentResponse

Result of incident response

**Campos:**
- `incident_id`
- `severity`
- `status`
- `actions_taken`
- `contained`
- `response_summary`

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
- `auto_contain`
- `severity_threshold`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
