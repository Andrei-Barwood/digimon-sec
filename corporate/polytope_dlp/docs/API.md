# API Reference - polytope_dlp

## Class: PolytopeDlp

### Constructor

```python
PolytopeDlp(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `detection_modes`: Configura detection_modes (Default: `["content", "context", "behavior"]`)
- `sensitivity_level`: Configura sensitivity_level (Default: `"medium"`)

### Métodos Principales

#### `scan_content(content, context)`

Escanea contenido en busca de violaciones de políticas.

Args:
    content: Contenido a escanear
    context: Contexto adicional (opcional)

Returns:
    Lista de PolicyViolation detectadas

#### `analyze(content, contents)`

Ejecuta análisis: un contenido o múltiples.

Args:
    content: Contenido individual
    contents: Lista de contenidos

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del módulo.



## Modelos de Datos

### ModuleConfig

Configuration model for polytope_dlp

**Campos:**
- `name`
- `detection_modes`
- `sensitivity_level`
- `enable_blocking`
- `alert_threshold`
- `debug`

### PolicyViolation

Policy violation information

**Campos:**
- `violation_id`
- `policy_name`
- `violation_type`
- `severity`
- `detected_data`
- `location`
- `timestamp`

### DLPAnalysis

Result of DLP analysis

**Campos:**
- `total_scanned`
- `violations_detected`
- `violations_by_severity`
- `violations_by_policy`
- `violations`
- `blocked_count`
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
- `detection_modes`
- `sensitivity_level`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
