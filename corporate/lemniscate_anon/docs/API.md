# API Reference - lemniscate_anon

## Class: LemniscateAnon

### Constructor

```python
LemniscateAnon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `anonymization_method`: Configura anonymization_method (Default: `"pseudonymize"`)

### Métodos Principales

#### `anonymize_field(field_name, value)`

Anonimiza un campo individual.

Args:
    field_name: Nombre del campo
    value: Valor a anonimizar

Returns:
    Valor anonimizado

#### `anonymize_data(data, fields_to_anonymize)`

Anonimiza un diccionario de datos.

Args:
    data: Datos a anonimizar
    fields_to_anonymize: Lista de campos a anonimizar (None = todos)

Returns:
    AnonymizationResult con resultados

#### `analyze(data, fields)`

Ejecuta análisis: anonimizar datos.

Args:
    data: Datos a anonimizar
    fields: Campos específicos a anonimizar (opcional)

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del módulo.



## Modelos de Datos

### ModuleConfig

Configuration model for lemniscate_anon

**Campos:**
- `name`
- `anonymization_method`
- `preserve_format`
- `reversible`
- `seed`
- `debug`

### AnonymizationRecord

Record of an anonymization operation

**Campos:**
- `record_id`
- `field_name`
- `original_value`
- `anonymized_value`
- `method`
- `reversible`

### AnonymizationResult

Result of anonymization operation

**Campos:**
- `original_data`
- `anonymized_data`
- `total_fields`
- `anonymized_fields`
- `anonymization_records`
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
- `anonymization_method`
- `reversible`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
