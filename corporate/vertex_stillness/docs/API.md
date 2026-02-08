# API Reference - vertex_stillness

## Class: VertexStillness

### Constructor

```python
VertexStillness(config: Optional[Dict[str, Any]] = None)
```

**Parametros de Configuracion:**

- `strict_mode`: Si True, falla ante settings criticos faltantes
- `require_flow_logs`: Requerir flow logs habilitados
- `require_nat_gateway`: Requerir NAT gateway
- `severity_threshold`: Severidad minima a reportar

### Metodos Principales

#### `audit_vpc(vpc_data)`

Audita configuraciones VPC y retorna un `AuditReport`.

#### `analyze(vpc_data)`

Ejecuta el analisis principal y retorna un `AnalysisResult`.

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Retorna metadata del módulo.

---

Ver tambien: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)

