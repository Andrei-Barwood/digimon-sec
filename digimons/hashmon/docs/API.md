# API Reference - hashmon

## Class: Hashmon

### Constructor

```python
Hashmon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `default_algorithm`: Configura default_algorithm (Default: `"sha256"`)
- `supported_algorithms`: Configura supported_algorithms (Default: `["md5", "sha1", "sha256", "sha512", "blake2b"]`)

### Métodos Principales

#### `compute_hash(data, algorithm, key)`

Calcula hash de datos.

Args:
    data: Datos a hashear
    algorithm: Algoritmo a usar (None = default)
    key: Clave para HMAC (opcional)

Returns:
    HashResult con resultado

#### `verify_hash(data, expected_hash, algorithm, key)`

Verifica hash de datos.

Args:
    data: Datos a verificar
    expected_hash: Hash esperado
    algorithm: Algoritmo a usar (None = default)
    key: Clave para HMAC (opcional)

Returns:
    VerificationResult con resultado

#### `analyze(data, expected_hash, algorithm, key)`

Ejecuta análisis: calcular o verificar hash.

Args:
    data: Datos a procesar
    expected_hash: Hash esperado (para verificación)
    algorithm: Algoritmo a usar
    key: Clave para HMAC (opcional)

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for hashmon

**Campos:**
- `name`
- `default_algorithm`
- `supported_algorithms`
- `enable_hmac`
- `chunk_size`
- `debug`

### HashResult

Hash computation result

**Campos:**
- `algorithm`
- `hash_value`
- `input_length`
- `computation_time_ms`
- `metadata`

### VerificationResult

Hash verification result

**Campos:**
- `verified`
- `algorithm`
- `expected_hash`
- `computed_hash`
- `match`
- `message`

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
- `default_algorithm`
- `supported_algorithms`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
