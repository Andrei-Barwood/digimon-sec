# API Reference - helix_filter

## Class: HelixFilter

### Constructor

```python
HelixFilter(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `threat_types`: Configura threat_types (Default: `["ip", "domain", "url", "hash", "email"]`)

### Métodos Principales

#### `analyze_threats(iocs)`

Analiza una lista de IOCs.

Args:
    iocs: Lista de IOCs a analizar

Returns:
    ThreatAnalysis con resultados

#### `analyze(iocs, ioc)`

Ejecuta análisis: un IOC o múltiples.

Args:
    iocs: Lista de IOCs
    ioc: IOC individual

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del módulo.



## Modelos de Datos

### ModuleConfig

Configuration model for helix_filter

**Campos:**
- `name`
- `threat_types`
- `confidence_threshold`
- `enable_reputation_check`
- `debug`

### IOCMatch

IOC match information

**Campos:**
- `ioc`
- `ioc_type`
- `threat_category`
- `confidence`
- `source`

### ThreatAnalysis

Result of threat analysis

**Campos:**
- `total_scanned`
- `threats_detected`
- `clean_count`
- `matches`
- `threats_by_type`
- `threats_by_category`
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
- `threat_types`
- `confidence_threshold`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
