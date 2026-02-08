# API Reference - vertex_vuln

## Class: VertexVuln

### Constructor

```python
VertexVuln(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `severity_threshold`: Configura severity_threshold (Default: `"medium"`)

### Métodos Principales

#### `scan_target(target)`

Escanea un objetivo en busca de vulnerabilidades.

Args:
    target: Objetivo a escanear (ej: "openssl-1.0.2")

Returns:
    ScanResult con vulnerabilidades encontradas

#### `analyze(target, targets)`

Ejecuta escaneo: un objetivo o múltiples.

Args:
    target: Objetivo individual a escanear
    targets: Lista de objetivos a escanear

Returns:
    AnalysisResult con resultados del escaneo

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del módulo.



## Modelos de Datos

### ModuleConfig

Configuration model for vertex_vuln

**Campos:**
- `name`
- `severity_threshold`
- `check_cves`
- `scan_depth`
- `debug`

### Vulnerability

Vulnerability information

**Campos:**
- `cve_id`
- `severity`
- `description`
- `affected_component`
- `recommendation`

### ScanResult

Result of vulnerability scan

**Campos:**
- `total_vulnerabilities`
- `critical_count`
- `high_count`
- `medium_count`
- `low_count`
- `vulnerabilities`
- `scan_summary`

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
- `severity_threshold`
- `scan_depth`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
