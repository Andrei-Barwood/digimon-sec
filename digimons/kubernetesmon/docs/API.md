# API Reference - kubernetesmon

## Class: Kubernetesmon

### Constructor

```python
Kubernetesmon(config: Optional[Dict[str, Any]] = None)
```

**Parametros de Configuracion:**

- `strict_mode`: Si True, falla ante settings criticos faltantes
- `require_rbac`: Requerir RBAC habilitado
- `require_psp`: Requerir pod security policies
- `require_etcd_encryption`: Requerir cifrado en etcd
- `severity_threshold`: Severidad minima a reportar

### Metodos Principales

#### `scan_cluster(cluster_data)`

Audita cluster Kubernetes y retorna un `AuditReport`.

#### `analyze(cluster_data)`

Ejecuta el analisis principal y retorna un `AnalysisResult`.

#### `validate(data)`

Valida datos de entrada.

#### `get_info()`

Retorna metadata del Digimon.

---

Ver tambien: [USAGE.md](USAGE.md), [ARCHITECTURE.md](ARCHITECTURE.md)
