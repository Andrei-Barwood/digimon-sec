# API Reference - Vertex Scan

## Class: VertexScan

### Constructor

```python
VertexScan(config: Optional[Dict[str, Any]] = None)
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

Obtener información del módulo

Returns:
    Diccionario con información



## Modelos de Datos

### ModuleConfig

Configuration model for Vertex Scan

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

### ModuleInfo

Information model for módulo metadata

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
