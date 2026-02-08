# Guía de Uso - Vertex Scan

## Inicio Rápido

### Instalación

```bash
pip install -e .
```

### Uso Básico

```python
from Vertex Scan.core import VertexScan

# Crear instancia
modulo = VertexScan()

# Ejecutar análisis principal
# Nota: Revise API.md para ver los argumentos específicos de analyze()
result = modulo.analyze()
print(result)
```

## Configuración Avanzada

Puede configurar Vertex Scan pasando un diccionario al constructor:

```python
modulo = VertexScan(config={
    # "opcion": "valor",  # Configuración específica
})
```

## Ejemplos de Uso

### Análisis Completo

```python
from Vertex Scan.core import VertexScan

modulo = VertexScan()

# Ejecutar análisis (ajuste los parámetros según sus necesidades)
result = modulo.analyze()

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
if modulo.validate(data):
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
