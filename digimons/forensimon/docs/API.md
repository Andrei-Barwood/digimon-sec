# API Reference - forensimon

## Class: Forensimon

### Constructor

```python
Forensimon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `supported_formats`: Configura supported_formats (Default: `[".log", ".txt", ".json", ".csv", ".xml"]`)

### Métodos Principales

#### `analyze_artifact(artifact_path)`

Analiza un artifact forense (archivo de log, etc).

Args:
    artifact_path: Ruta al artifact a analizar

Returns:
    ArtifactAnalysis con resultados del análisis

#### `analyze(artifact_path, artifact_paths)`

Ejecuta análisis forense: un artifact o múltiples.

Args:
    artifact_path: Ruta a un artifact individual
    artifact_paths: Lista de rutas a múltiples artifacts

Returns:
    AnalysisResult con resultados del análisis

#### `validate(data)`

Valida datos de entrada (string o lista de strings).

#### `get_info()`

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for forensimon

**Campos:**
- `name`
- `max_file_size_mb`
- `supported_formats`
- `extract_timestamps`
- `extract_ips`
- `extract_emails`
- `debug`

### ArtifactAnalysis

Result of artifact analysis

**Campos:**
- `artifact_path`
- `artifact_type`
- `file_size`
- `line_count`
- `timestamps_found`
- `ips_found`
- `emails_found`
- `suspicious_patterns`
- `analysis_summary`

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
- `max_file_size_mb`
- `supported_formats`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
