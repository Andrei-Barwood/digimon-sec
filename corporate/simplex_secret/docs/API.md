# API Reference - simplex_secret

## Class: SimplexSecret

### Constructor

```python
SimplexSecret(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `redaction_mode`: Configura redaction_mode (Default: `"mask"`)

### Métodos Principales

#### `redact_pii(text)`

Redacta PII de un texto.

Args:
    text: Texto a redactar

Returns:
    RedactionResult con resultados

#### `analyze(text, texts)`

Ejecuta análisis: un texto o múltiples.

Args:
    text: Texto individual
    texts: Lista de textos

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del módulo.



## Modelos de Datos

### ModuleConfig

Configuration model for simplex_secret

**Campos:**
- `name`
- `redaction_mode`
- `preserve_format`
- `enable_ip_detection`
- `enable_ssn_detection`
- `enable_phone_detection`
- `debug`

### RedactionResult

Result of data redaction

**Campos:**
- `original_text`
- `safe_text`
- `redacted_items`
- `statistics`
- `total_redacted`

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
- `redaction_mode`
- `supported_types`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
