# Guia de Uso - polytope_cluster

## Tutorial Paso a Paso

Este tutorial muestra como usar **PolytopeCluster** para cluster Kubernetes.

### 1) Instalacion rapida

```bash
pip install -e .
```

### 2) Importacion e inicializacion

```python
from polytope_cluster.core import PolytopeCluster

modulo = PolytopeCluster()
```

### 3) Preparar los datos de entrada

```python
cluster_data = {
    "rbac_enabled": True,
    "pod_security_policies": True,
    "etcd_encryption": True,
    "public_api": False,
}
```

### 4) Validar los datos (opcional)

```python
if not modulo.validate(cluster_data):
    raise ValueError("Datos invalidos")
```

### 5) Ejecutar el analisis

```python
result = modulo.analyze(cluster_data=cluster_data)
print(result.status)
print(result.message)
```

---

Ver tambien: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)
