# Arquitectura - Ciphermon (Mega)

## Visión General

Ciphermon valida políticas de cifrado modernas y ofrece utilidades seguras para llaves e integridad.

**Misión**: American Venom  
**Rol**: encryption-expert

## Componentes

### 1. Core (`core.py`)
- `Ciphermon` con:
  - `check_policy()` valida tamaño de llave, AEAD y ciphers legacy.
  - `generate_key()` genera llaves seguras (base64 urlsafe).
  - `encrypt()/decrypt()` cifrado simulado + HMAC-SHA256 para integridad.
  - `analyze()` orquesta política + cifrado opcional.

### 2. Models (`models.py`)
- `DigimonConfig`, `PolicyCheck`, `EncryptionResult`, `AnalysisResult`, `DigimonInfo`.

### 3. Utils (`utils.py`)
- `setup_logging`, `format_result`.

## Flujo
1) Se validan parámetros de política (cipher, key_bits, AEAD).  
2) Opcionalmente se cifra el plaintext y se devuelve HMAC para integridad.  
3) `analyze` retorna estado, data tipada y errores si aplica.

## Seguridad (2025-2026)
- Mínimo 256 bits por defecto, AEAD requerido.
- Alertas sobre DES/RC4/3DES/AES-128 si `allow_legacy` es falso.
- HMAC-SHA256 para integridad de ejemplo; no guarda llaves en disco.
# Arquitectura - ciphermon

## Visión General

ciphermon es un módulo de ciberseguridad implementado como parte del **DIGIMON CYBERSECURITY SUITE**.

**Misión**: American Venom  
**Rol de Seguridad**: Encryption Expert

## Componentes Principales

### 1. Core Module (`core.py`)

Contiene la clase principal `Ciphermon` que implementa la lógica central.

- `__init__()` - Inicialización
- `analyze()` - Análisis principal
- `validate()` - Validación de datos
- `get_info()` - Metadata del Digimon

### 2. Models (`models.py`)

Define tipos y esquemas usando Pydantic:
- `DigimonConfig` - Configuración
- `AnalysisResult` - Resultados
- `DigimonInfo` - Información

### 3. Utils (`utils.py`)

- `setup_logging()` - Configurar logging
- `format_result()` - Formatear resultados
- `validate_input()` - Validar tipos

---

Ver también: [README.md](../README.md), [USAGE.md](USAGE.md)
