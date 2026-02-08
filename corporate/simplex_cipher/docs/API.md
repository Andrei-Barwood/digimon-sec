# API Reference - simplex_cipher

## Class: SimplexCipher

### Constructor

```python
SimplexCipher(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `default_cipher`: Configura default_cipher (Default: `"AES-256-GCM"`)

### Métodos Principales

#### `generate_key(bits)`

Genera una llave aleatoria con el tamaño solicitado (bits).

#### `encrypt(plaintext, key)`

Cifra de forma simulada y devuelve datos + HMAC.

#### `decrypt(ciphertext_b64, key)`

Descifra simulando (base64) y verifica HMAC.

#### `check_policy(cipher, key_bits, aead)`

Sin documentación.

#### `analyze(cipher, key_bits, aead, plaintext)`

Evalúa política de cifrado y opcionalmente ejecuta cifrado simulado.

#### `validate(data)`

Sin documentación.

#### `get_info()`

Sin documentación.



## Modelos de Datos

### ModuleConfig

Configuration model for simplex_cipher.

**Campos:**
- `name`
- `default_cipher`
- `min_key_bits`
- `allow_legacy`
- `require_aead`
- `debug`

### PolicyCheck

Result of a crypto policy evaluation.

**Campos:**
- `cipher`
- `key_bits`
- `aead`
- `compliant`
- `warnings`
- `errors`

### EncryptionResult

Result of encrypt/decrypt helper.

**Campos:**
- `status`
- `message`
- `data`
- `errors`

### AnalysisResult

High-level analysis output.

**Campos:**
- `status`
- `message`
- `data`
- `errors`

### ModuleInfo

Information model for módulo metadata.

**Campos:**
- `name`
- `mission`
- `role`
- `status`
- `default_cipher`
- `min_key_bits`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
