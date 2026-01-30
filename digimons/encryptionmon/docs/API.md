# API Reference - encryptionmon

## Class: Encryptionmon

### Constructor

```python
Encryptionmon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `default_algorithm`: Configura default_algorithm (Default: `"AES-256-GCM"`)
- `key_storage_backend`: Configura key_storage_backend (Default: `"memory"`)

### Métodos Principales

#### `generate_key(algorithm, key_type)`

Genera una nueva clave de cifrado.

Args:
    algorithm: Algoritmo a usar (None = default)
    key_type: Tipo de clave (symmetric/asymmetric)

Returns:
    EncryptionKey generada

#### `rotate_key(key_id)`

Rota una clave existente.

Args:
    key_id: ID de la clave a rotar

Returns:
    KeyManagementResult con resultado

#### `revoke_key(key_id)`

Revoca una clave.

Args:
    key_id: ID de la clave a revocar

Returns:
    KeyManagementResult con resultado

#### `list_keys()`

Lista todas las claves activas.

Returns:
    Lista de EncryptionKey

#### `check_expired_keys()`

Verifica claves expiradas.

Returns:
    Lista de IDs de claves expiradas

#### `analyze(operation, key_id)`

Ejecuta análisis: operaciones de gestión de claves.

Args:
    operation: Operación a realizar (generate/rotate/revoke/list)
    key_id: ID de clave (para rotate/revoke)

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for encryptionmon

**Campos:**
- `name`
- `default_algorithm`
- `key_rotation_days`
- `key_storage_backend`
- `enable_key_derivation`
- `debug`

### EncryptionKey

Encryption key information

**Campos:**
- `key_id`
- `algorithm`
- `key_type`
- `created_at`
- `expires_at`
- `rotation_count`
- `metadata`

### KeyManagementResult

Result of key management operation

**Campos:**
- `operation`
- `key_id`
- `success`
- `message`
- `keys_active`
- `keys_rotated`
- `keys_revoked`

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
- `key_rotation_days`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
