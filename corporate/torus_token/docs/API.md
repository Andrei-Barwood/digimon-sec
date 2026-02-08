# API Reference - torus_token

## Class: TorusToken

### Constructor

```python
TorusToken(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `token_type`: Configura token_type (Default: `"JWT"`)
- `algorithm`: Configura algorithm (Default: `"HS256"`)

### Métodos Principales

#### `generate_token(claims, expiration_hours)`

Genera un token seguro.

Args:
    claims: Claims/payload del token
    expiration_hours: Horas hasta expiración (opcional)

Returns:
    TokenResult con token generado

#### `validate_token(token)`

Valida un token.

Args:
    token: Token a validar

Returns:
    TokenResult con resultado de validación

#### `analyze(action, claims, token)`

Ejecuta análisis: generar o validar token.

Args:
    action: Acción ("generate" o "validate")
    claims: Claims para generar (si action="generate")
    token: Token para validar (si action="validate")

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del módulo.



## Modelos de Datos

### ModuleConfig

Configuration model for torus_token

**Campos:**
- `name`
- `token_type`
- `algorithm`
- `expiration_hours`
- `secret_length`
- `debug`

### TokenResult

Result of token generation/validation

**Campos:**
- `token`
- `token_type`
- `algorithm`
- `expires_at`
- `valid`
- `claims`
- `errors`

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
- `token_type`
- `algorithm`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
