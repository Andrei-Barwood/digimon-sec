# API Reference - lattice_permission

## Class: LatticePermission

### Constructor

```python
LatticePermission(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- No hay parámetros de configuración específicos documentados.

### Métodos Principales

#### `check_permission(resource, required_permission)`

Verifica permisos de un recurso.

Args:
    resource: Ruta al recurso
    required_permission: Permiso requerido (read/write/execute)

Returns:
    PermissionCheck con resultado

#### `analyze(resource, resources)`

Ejecuta análisis: un recurso o múltiples.

Args:
    resource: Recurso individual
    resources: Lista de recursos con permisos requeridos

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del módulo.



## Modelos de Datos

### ModuleConfig

Configuration model for lattice_permission

**Campos:**
- `name`
- `check_file_permissions`
- `check_directory_permissions`
- `enforce_least_privilege`
- `debug`

### PermissionCheck

Result of permission check

**Campos:**
- `resource`
- `resource_type`
- `required_permission`
- `granted`
- `current_permissions`
- `violations`

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
- `enforce_least_privilege`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
