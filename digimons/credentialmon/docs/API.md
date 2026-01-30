# API Reference - credentialmon

## Class: Credentialmon

### Constructor

```python
Credentialmon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `hash_algorithm`: Configura hash_algorithm (Default: `"sha256"`)

### Métodos Principales

#### `store_credential(credential_id, username, service, password)`

Almacena una credencial de forma segura.

Args:
    credential_id: ID único de la credencial
    username: Nombre de usuario (opcional)
    service: Nombre del servicio
    password: Contraseña (se hasheará/encriptará)

Returns:
    Credential almacenada

#### `analyze_vault()`

Analiza el vault de credenciales.

Returns:
    CredentialVault con análisis

#### `analyze(action, credential_data)`

Ejecuta análisis: analizar vault o almacenar credencial.

Args:
    action: Acción ("analyze" o "store")
    credential_data: Datos de credencial (si action="store")

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for credentialmon

**Campos:**
- `name`
- `encryption_enabled`
- `key_rotation_days`
- `hash_algorithm`
- `debug`

### Credential

Credential information

**Campos:**
- `credential_id`
- `username`
- `service`
- `encrypted`
- `created_at`
- `last_rotated`

### CredentialVault

Credential vault analysis

**Campos:**
- `total_credentials`
- `encrypted_count`
- `unencrypted_count`
- `expired_keys`
- `credentials`
- `vault_summary`

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
- `encryption_enabled`
- `key_rotation_days`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
