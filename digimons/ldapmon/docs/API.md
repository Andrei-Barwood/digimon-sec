# API Reference - ldapmon

## Class: LDAPmon

### Constructor

```python
LDAPmon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- No hay parámetros de configuración específicos documentados.

### Métodos Principales

#### `search_entries(filter_str, attributes)`

Busca entradas LDAP.

Args:
    filter_str: Filtro LDAP (default: "(objectClass=*)")
    attributes: Atributos a retornar (opcional)

Returns:
    Lista de LDAPEntry encontradas

#### `analyze_directory()`

Analiza el directorio LDAP.

Returns:
    LDAPAnalysis con resultados

#### `analyze(action, search_data)`

Ejecuta análisis: analizar directorio o buscar entradas.

Args:
    action: Acción ("analyze" o "search")
    search_data: Datos de búsqueda (si action="search")

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for ldapmon

**Campos:**
- `name`
- `ldap_url`
- `base_dn`
- `use_tls`
- `timeout`
- `debug`

### LDAPEntry

LDAP directory entry

**Campos:**
- `dn`
- `attributes`
- `entry_type`

### LDAPAnalysis

Result of LDAP analysis

**Campos:**
- `total_entries`
- `entries_by_type`
- `connection_status`
- `violations`
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
- `use_tls`
- `timeout`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
