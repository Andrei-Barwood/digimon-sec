# API Reference - mfamon

## Class: MFAmon

### Constructor

```python
MFAmon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `mfa_methods`: Configura mfa_methods (Default: `["totp", "sms", "email", "push"]`)
- `default_method`: Configura default_method (Default: `"totp"`)

### Métodos Principales

#### `generate_code(length)`

Genera código numérico para MFA.

#### `create_challenge(user_id, method)`

Crea un desafío MFA.

Args:
    user_id: ID del usuario
    method: Método MFA (opcional, usa default si no se especifica)

Returns:
    MFAChallenge creado

#### `verify_challenge(challenge_id, code)`

Verifica un código MFA.

Args:
    challenge_id: ID del desafío
    code: Código a verificar

Returns:
    True si el código es válido

#### `analyze_mfa()`

Analiza todos los desafíos MFA.

Returns:
    MFAAnalysis con resultados

#### `analyze(action, challenge_data)`

Ejecuta análisis: analizar MFA o crear desafío.

Args:
    action: Acción ("analyze" o "create")
    challenge_data: Datos del desafío (si action="create")

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for mfamon

**Campos:**
- `name`
- `mfa_methods`
- `default_method`
- `code_expiry`
- `max_attempts`
- `debug`

### MFAChallenge

MFA challenge information

**Campos:**
- `challenge_id`
- `user_id`
- `method`
- `code`
- `expires_at`
- `verified`
- `attempts`

### MFAAnalysis

Result of MFA analysis

**Campos:**
- `total_challenges`
- `verified_count`
- `pending_count`
- `failed_count`
- `methods_usage`
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
- `mfa_methods`
- `default_method`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
