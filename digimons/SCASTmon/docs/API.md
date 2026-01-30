# API Reference - SCASTmon

## Class: Scastmon

### Constructor

```python
Scastmon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- No hay parámetros de configuración específicos documentados.

### Métodos Principales

#### `analyze()`

Ejecutar análisis principal

Returns:
    Diccionario con resultados del análisis

#### `validate(data)`

Validar datos de entrada

Args:
    data: Datos a validar

Returns:
    True si válido, False en caso contrario

#### `get_info()`

Obtener información del Digimon

Returns:
    Diccionario con información



## Modelos de Datos

### DigimonConfig

Configuration model for SCASTmon

**Campos:**
- `name`
- `debug`
- `timeout`

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
- `version`

### Config

Pydantic config




---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
