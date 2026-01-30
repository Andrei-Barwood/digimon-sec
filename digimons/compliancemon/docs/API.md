# API Reference - compliancemon

## Class: Compliancemon

### Constructor

```python
Compliancemon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- `compliance_frameworks`: Configura compliance_frameworks (Default: `["GDPR", "HIPAA", "PCI-DSS", "SOX", "ISO27001"]`)
- `report_format`: Configura report_format (Default: `"json"`)

### Métodos Principales

#### `audit_target(target_data)`

Audita un objetivo para cumplimiento.

Args:
    target_data: Datos del objetivo a auditar

Returns:
    ComplianceAudit con resultados

#### `analyze(target_data)`

Ejecuta análisis: auditoría de compliance.

Args:
    target_data: Datos del objetivo a auditar

Returns:
    AnalysisResult con resultados

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Obtener información del Digimon.



## Modelos de Datos

### DigimonConfig

Configuration model for compliancemon

**Campos:**
- `name`
- `compliance_frameworks`
- `strict_mode`
- `auto_remediation`
- `report_format`
- `debug`

### ComplianceCheck

Individual compliance check result

**Campos:**
- `check_id`
- `framework`
- `requirement`
- `status`
- `severity`
- `description`
- `remediation`
- `evidence`

### ComplianceAudit

Result of compliance audit

**Campos:**
- `audit_id`
- `frameworks_checked`
- `total_checks`
- `passed_checks`
- `failed_checks`
- `warning_checks`
- `compliance_score`
- `checks`
- `summary`

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
- `compliance_frameworks`
- `strict_mode`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
