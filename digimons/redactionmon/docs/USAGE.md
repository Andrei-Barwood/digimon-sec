# Guía de Uso - redactionmon

## Inicio Rápido

### Instalación

```bash
pip install -e .
```

### Uso Básico

```python
from redactionmon.core import Redactionmon

# Crear instancia
digimon = Redactionmon()

# Ejecutar análisis principal
# Nota: Revise API.md para ver los argumentos específicos de analyze()
result = digimon.analyze()
print(result)
```

## Configuración Avanzada

Puede configurar redactionmon pasando un diccionario al constructor:

```python
digimon = Redactionmon(config={
    "redaction_style": "mask",  # Configura redaction_style
    "pii_types": ["email", "phone", "ssn", "credit_card", "ip"],  # Configura pii_types
})
```

## Ejemplos de Uso

### Análisis Completo

```python
from redactionmon.core import Redactionmon

digimon = Redactionmon()

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
