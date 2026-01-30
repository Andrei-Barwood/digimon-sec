# API Reference - pci-dssmon

## Class: PCI_DSSmon

### Constructor

```python
PCI_DSSmon(config: Optional[Dict[str, Any]] = None)
```

**Parámetros de Configuración:**

- No hay parámetros de configuración específicos documentados.

### Métodos Principales

#### `audit_compliance(target_data)`

Audita cumplimiento PCI-DSS de un objetivo.

Args:
    target_data: Datos del objetivo a auditar

Returns:
    PCI_DSSComplianceReport con resultados

#### `analyze(target_data)`

Ejecuta análisis: auditoría PCI-DSS.

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

Configuration model for pci_dssmon

**Campos:**
- `name`
- `strict_mode`
- `check_card_data_protection`
- `check_network_segmentation`
- `check_vulnerability_management`
- `debug`

### PCI_DSSCheck

Individual PCI-DSS compliance check result

**Campos:**
- `check_id`
- `requirement`
- `description`
- `status`
- `severity`
- `remediation`
- `evidence`

### PCI_DSSComplianceReport

PCI-DSS compliance report

**Campos:**
- `report_id`
- `total_checks`
- `passed_checks`
- `failed_checks`
- `warning_checks`
- `compliance_score`
- `checks`
- `card_data_protection_status`
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
- `strict_mode`
- `version`



---

Ver también: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
