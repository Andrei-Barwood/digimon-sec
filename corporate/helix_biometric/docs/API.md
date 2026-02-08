# API Reference - helix_biometric

## Class: HelixBiometric

### Constructor

```python
HelixBiometric(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `supported_types`: Configura supported_types (Default: `["fingerprint", "face", "iris", "voice"]`)

### Métodos Principales

#### `register_biometric(user_id, biometric_type, template_data, confidence, liveness_verified)`

Registra un template biométrico.

Args:
    user_id: ID del usuario
    biometric_type: Tipo de biométrico
    template_data: Datos del template (simulado como string)
    confidence: Nivel de confianza (0.0-1.0)
    liveness_verified: Si liveness fue verificado

Returns:
    BiometricData registrado

#### `analyze_biometrics()`

Analiza todos los templates biométricos.

Returns:
    BiometricAnalysis con resultados

#### `analyze(action, biometric_data)`

Ejecuta análisis: analizar templates o registrar nuevo.

Args:
    action: Acción ("analyze" o "register")
    biometric_data: Datos biométricos (si action="register")

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del módulo.



## Modelos de Datos

### ModuleConfig

Configuration model for helix_biometric

**Campos:**
- `name`
- `supported_types`
- `min_confidence`
- `enable_liveness`
- `debug`

### BiometricData

Biometric data information

**Campos:**
- `biometric_id`
- `user_id`
- `biometric_type`
- `template_hash`
- `confidence`
- `liveness_verified`
- `created_at`

### BiometricAnalysis

Result of biometric analysis

**Campos:**
- `total_templates`
- `templates_by_type`
- `low_confidence`
- `liveness_verified`
- `violations`
- `analysis_summary`

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
- `supported_types`
- `min_confidence`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
