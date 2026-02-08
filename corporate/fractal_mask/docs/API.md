# API Reference - fractal_mask

## Class: FractalMask

### Constructor

```python
FractalMask(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `mask_character`: Configura mask_character (Default: `"*"`)
- `pii_types`: Configura pii_types (Default: `["email", "phone", "credit_card", "ssn", "ip"]`)

### Métodos Principales

#### `mask_text(text)`

Enmascara PII de un texto.

Args:
    text: Texto a enmascarar

Returns:
    MaskingResult con resultados

#### `analyze(text, texts)`

Ejecuta análisis: enmascarar texto(s).

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

Configuration model for fractal_mask

**Campos:**
- `name`
- `mask_character`
- `mask_length`
- `preserve_format`
- `pii_types`
- `log_context`
- `debug`

### MaskingRecord

Record of a masking operation

**Campos:**
- `record_id`
- `pii_type`
- `original_value`
- `masked_value`
- `position`
- `preserve_format`

### MaskingResult

Result of masking operation

**Campos:**
- `original_text`
- `masked_text`
- `total_masked`
- `masked_by_type`
- `masking_records`
- `statistics`

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
- `mask_character`
- `pii_types`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
