# API Reference - torus_log

## Class: TorusLog

### Constructor

```python
TorusLog(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `log_levels`: Configura log_levels (Default: `["ERROR", "WARN", "INFO", "DEBUG"]`)

### Métodos Principales

#### `parse_log_entry(log_line, source)`

Parsea una línea de log.

Args:
    log_line: Línea de log a parsear
    source: Fuente del log (opcional)

Returns:
    LogEntry o None si no se puede parsear

#### `analyze_logs(log_lines, source)`

Analiza múltiples líneas de log.

Args:
    log_lines: Lista de líneas de log
    source: Fuente del log (opcional)

Returns:
    LogAnalysis con resultados

#### `analyze(log_data, log_lines)`

Ejecuta análisis: string o lista de líneas.

Args:
    log_data: String con logs (será dividido en líneas)
    log_lines: Lista de líneas de log

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del módulo.



## Modelos de Datos

### ModuleConfig

Configuration model for torus_log

**Campos:**
- `name`
- `log_levels`
- `pattern_detection`
- `correlation_window`
- `debug`

### LogEntry

Log entry information

**Campos:**
- `timestamp`
- `level`
- `message`
- `source`
- `metadata`

### LogAnalysis

Result of log analysis

**Campos:**
- `total_entries`
- `entries_by_level`
- `patterns_detected`
- `errors_found`
- `warnings_found`
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
- `log_levels`
- `correlation_window`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
