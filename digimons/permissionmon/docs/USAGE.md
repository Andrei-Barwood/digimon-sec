# Guía de Uso - permissionmon

## Inicio Rápido

### Instalación

```bash
pip install -e .
```

### Uso Básico

```python
from permissionmon.core import Permissionmon

# Crear instancia
digimon = Permissionmon()

# Ejecutar análisis principal
# Nota: Revise API.md para ver los argumentos específicos de analyze()
result = digimon.analyze()
print(result)
```

## Configuración Avanzada

Puede configurar permissionmon pasando un diccionario al constructor:

```python
digimon = Permissionmon(config={
    # "opcion": "valor",  # Configuración específica
})
```

## Ejemplos de Uso

### Análisis Completo

```python
from permissionmon.core import Permissionmon

digimon = Permissionmon()

# Ejecutar análisis (ajuste los parámetros según sus necesidades)
result = digimon.analyze()

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
if digimon.validate(data):
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
