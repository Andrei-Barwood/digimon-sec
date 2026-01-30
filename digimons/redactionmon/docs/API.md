# API Reference - redactionmon

## Class: Redactionmon

### Constructor

```python
Redactionmon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `redaction_style`: Configura redaction_style (Default: `"mask"`)
- `pii_types`: Configura pii_types (Default: `["email", "phone", "ssn", "credit_card", "ip"]`)

### Métodos Principales

#### `redact_text(text)`

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

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for redactionmon

**Campos:**
- `name`
- `redaction_style`
- `preserve_structure`
- `pii_types`
- `debug`

### RedactionRecord

Record of a redaction operation

**Campos:**
- `record_id`
- `pii_type`
- `original_value`
- `redacted_value`
- `position`
- `confidence`

### RedactionResult

Result of redaction operation

**Campos:**
- `original_text`
- `redacted_text`
- `total_redactions`
- `redactions_by_type`
- `redaction_records`
- `statistics`

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
- `redaction_style`
- `pii_types`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
