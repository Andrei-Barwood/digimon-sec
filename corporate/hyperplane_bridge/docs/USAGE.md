# Guía de Uso - hyperplane_bridge

## Inicio Rápido

### Instalación

```bash
pip install -e .
```

### Uso Básico

```python
from hyperplane_bridge.core import HyperplaneBridge

# Crear instancia
mod = HyperplaneBridge()

# Ejecutar análisis principal
# Nota: Revise API.md para ver los argumentos específicos de analyze()
result = mod.analyze()
print(result)
```

## Configuración Avanzada

Puede configurar hyperplane_bridge pasando un diccionario al constructor:

```python
mod = HyperplaneBridge(config={
    "severity_threshold": "medium",  # Configura severity_threshold
})
```

## Ejemplos de Uso

### Análisis Completo

```python
from hyperplane_bridge.core import HyperplaneBridge

mod = HyperplaneBridge()

# Ejecutar análisis (ajuste los parámetros según sus necesidades)
result = mod.analyze()

if result.status == "success":
    print(f"Operación exitosa: {result.message}")
    print("Datos:", result.data)
elif result.status == "warning":
    print(f"Advertencia: {result.message}")
else:
    print(f"Error: {result.message}")
    print("Errores:", result.errors)
```

### Validación de Datos

```python
data = "..." # Datos a validar
if mod.validate(data):
    print("Datos válidos para procesamiento")
else:
    print("Datos inválidos")
```

## Mejores Prácticas (2025-2026)

1. **Configuración Mínima**: Comience con la configuración por defecto y ajuste según necesidad.
2. **Manejo de Errores**: Verifique siempre `result.status` antes de procesar `result.data`.
3. **Logs**: Configure el nivel de logging adecuado para producción vs desarrollo.
4. **Validación**: Use el método `validate()` antes de procesar datos externos no confiables.

---

Ver también: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)
