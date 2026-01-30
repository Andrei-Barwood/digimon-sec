# API Reference - networkmon

## Class: Networkmon

### Constructor

```python
Networkmon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- No hay parámetros de configuración específicos documentados.

### Métodos Principales

#### `add_connection(source_ip, dest_ip, source_port, dest_port, protocol)`

Añade una conexión al monitor.

Args:
    source_ip: IP de origen
    dest_ip: IP de destino
    source_port: Puerto de origen (opcional)
    dest_port: Puerto de destino (opcional)
    protocol: Protocolo (opcional)

#### `analyze_traffic()`

Analiza el tráfico acumulado.

Returns:
    TrafficAnalysis con resultados del análisis

#### `analyze(connections)`

Analiza tráfico: usa conexiones existentes o acepta nuevas.

Args:
    connections: Lista opcional de conexiones a analizar

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del Digimon.

#### `reset()`

Resetea el estado del monitor.



## Modelos de Datos

### DigimonConfig

Configuration model for networkmon

**Campos:**
- `name`
- `max_connections`
- `alert_threshold`
- `track_ports`
- `track_protocols`
- `debug`

### NetworkConnection

Network connection information

**Campos:**
- `source_ip`
- `dest_ip`
- `source_port`
- `dest_port`
- `protocol`
- `timestamp`

### TrafficAnalysis

Result of traffic analysis

**Campos:**
- `total_connections`
- `unique_ips`
- `port_usage`
- `protocol_usage`
- `suspicious_connections`
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
- `max_connections`
- `alert_threshold`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
