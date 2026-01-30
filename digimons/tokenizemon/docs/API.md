# API Reference - tokenizemon

## Class: Tokenizemon

### Constructor

```python
Tokenizemon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `token_format`: Configura token_format (Default: `"uuid"`)
- `token_mapping_backend`: Configura token_mapping_backend (Default: `"memory"`)

### Métodos Principales

#### `tokenize_value(value)`

Tokeniza un valor individual.

Args:
    value: Valor a tokenizar

Returns:
    Token generado

#### `tokenize_text(text, pii_patterns)`

Tokeniza PII en un texto.

Args:
    text: Texto a tokenizar
    pii_patterns: Patrones PII personalizados (opcional)

Returns:
    TokenizationResult con resultados

#### `detokenize(token)`

Detokeniza un token.

Args:
    token: Token a detokenizar

Returns:
    DetokenizationResult con resultado

#### `analyze(text, token)`

Ejecuta análisis: tokenizar texto o detokenizar token.

Args:
    text: Texto a tokenizar
    token: Token a detokenizar

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for tokenizemon

**Campos:**
- `name`
- `token_format`
- `preserve_format`
- `token_mapping_backend`
- `enable_detokenization`
- `token_prefix`
- `debug`

### TokenizationRecord

Record of a tokenization operation

**Campos:**
- `record_id`
- `original_value`
- `token`
- `token_type`
- `created_at`
- `reversible`

### TokenizationResult

Result of tokenization operation

**Campos:**
- `original_data`
- `tokenized_data`
- `total_tokens`
- `tokens_by_type`
- `tokenization_records`
- `statistics`

### DetokenizationResult

Result of detokenization operation

**Campos:**
- `token`
- `original_value`
- `found`
- `message`

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
- `token_format`
- `enable_detokenization`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
