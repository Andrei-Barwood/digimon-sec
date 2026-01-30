# API Reference - passwordmon

## Class: Passwordmon

### Constructor

```python
Passwordmon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- No hay parámetros de configuración específicos documentados.

### Métodos Principales

#### `validate_password(password)`

Valida una contraseña.

Args:
    password: Contraseña a validar

Returns:
    PasswordValidation con resultado

#### `analyze(password, passwords)`

Ejecuta análisis: una contraseña o múltiples.

Args:
    password: Contraseña individual
    passwords: Lista de contraseñas

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for passwordmon

**Campos:**
- `name`
- `min_length`
- `require_uppercase`
- `require_lowercase`
- `require_numbers`
- `require_special`
- `check_common_passwords`
- `debug`

### PasswordValidation

Result of password validation

**Campos:**
- `password`
- `valid`
- `strength`
- `score`
- `violations`
- `recommendations`

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
- `min_length`
- `require_special`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
