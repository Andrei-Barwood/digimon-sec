# API Reference - Ciphermon (Mega)

## Class: Ciphermon

### Constructor
```python
Ciphermon(config: Optional[Dict[str, Any]] = None)
```
Config keys:
- `default_cipher`: str, default "AES-256-GCM"
- `min_key_bits`: int, default 256
- `allow_legacy`: bool, default False
- `require_aead`: bool, default True

### Métodos
- `generate_key(bits=None) -> str`  
  Llave aleatoria urlsafe base64.

- `encrypt(plaintext, key=None) -> EncryptionResult`  
  Cifrado simulado + HMAC-SHA256.

- `decrypt(ciphertext_b64, key) -> EncryptionResult`  
  Descifrado simulado + HMAC.

- `check_policy(cipher, key_bits, aead) -> PolicyCheck`  
  Valida tamaño, AEAD y legacy.

- `analyze(cipher=None, key_bits=None, aead=None, plaintext=None) -> AnalysisResult`  
  Ejecuta política y opcional cifrado simulado.

- `validate(data) -> bool`  
  Valida entrada básica.

- `get_info() -> dict`  
  Metadata del Digimon.
# API Reference - ciphermon

## Class: Ciphermon

### Constructor

```python
Ciphermon(config: Optional[Dict[str, Any]] = None)
```

### Methods

- `analyze()` - Execute main analysis
- `validate(data)` - Validate input data
- `get_info()` - Get Digimon metadata

---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
