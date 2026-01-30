# API Reference - fuzzymon

## Class: Fuzzymon

### Constructor

```python
Fuzzymon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- No hay parámetros de configuración específicos documentados.

### Métodos Principales

#### `generate_fuzz_input(base_input)`

Genera una entrada fuzzed.

Args:
    base_input: Entrada base para mutar (opcional)

Returns:
    String con entrada fuzzed

#### `fuzz_target(target_function, base_input)`

Ejecuta fuzzing en un objetivo.

Args:
    target_function: Función a fuzzear (opcional, simulado)
    base_input: Entrada base (opcional)

Returns:
    FuzzResult con resultados

#### `analyze(target_function, base_input, iterations)`

Ejecuta análisis de fuzzing.

Args:
    target_function: Función a fuzzear (opcional)
    base_input: Entrada base (opcional)
    iterations: Número de iteraciones (opcional)

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for fuzzymon

**Campos:**
- `name`
- `max_iterations`
- `mutation_rate`
- `timeout_seconds`
- `debug`

### FuzzResult

Result of fuzzing operation

**Campos:**
- `total_tests`
- `crashes_found`
- `hangs_found`
- `bugs_found`
- `coverage_percent`
- `fuzz_summary`

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
- `max_iterations`
- `mutation_rate`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
