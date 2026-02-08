# API Reference - hyperplane_crawl

## Class: HyperplaneCrawl

### Constructor

```python
HyperplaneCrawl(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `detection_methods`: Configura detection_methods (Default: `["rate_limit", "user_agent", "pattern", "behavior"]`)
- `suspicious_patterns`: Configura suspicious_patterns (Default: `["bot", "crawler", "scraper", "spider"]`)

### Métodos Principales

#### `analyze_request(ip_address, user_agent)`

Analiza una request individual.

Args:
    ip_address: IP de la request
    user_agent: User agent string

Returns:
    ScrapingAttempt con resultado

#### `analyze(requests)`

Ejecuta análisis: analizar requests.

Args:
    requests: Lista de requests con 'ip_address' y 'user_agent'

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del módulo.



## Modelos de Datos

### ModuleConfig

Configuration model for hyperplane_crawl

**Campos:**
- `name`
- `detection_methods`
- `rate_limit_threshold`
- `block_duration_minutes`
- `enable_captcha`
- `suspicious_patterns`
- `debug`

### ScrapingAttempt

Scraping attempt information

**Campos:**
- `attempt_id`
- `ip_address`
- `user_agent`
- `request_count`
- `detection_method`
- `severity`
- `timestamp`
- `blocked`

### ScrapingAnalysis

Result of scraping analysis

**Campos:**
- `total_requests`
- `scraping_attempts`
- `blocked_attempts`
- `attempts_by_severity`
- `attempts_by_method`
- `attempts`
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
- `detection_methods`
- `rate_limit_threshold`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
