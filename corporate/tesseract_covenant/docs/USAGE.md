# Guía de Uso - tesseract_covenant

## Inicio Rápido

### Instalación

```bash
pip install -e .
```

### Uso Básico

```python
from tesseract_covenant.core import TesseractCovenant

# Crear instancia
modulo = TesseractCovenant()

# Ejecutar análisis principal
# Nota: Revise API.md para ver los argumentos específicos de analyze()
result = modulo.analyze()
print(result)
```

## Configuración Avanzada

Puede configurar tesseract_covenant pasando un diccionario al constructor:

```python
modulo = TesseractCovenant(config={
    "compliance_frameworks": ["GDPR", "HIPAA", "PCI-DSS", "SOX", "ISO27001"],  # Configura compliance_frameworks
    "report_format": "json",  # Configura report_format
})
```

## Ejemplos de Uso

### Análisis Completo

```python
from tesseract_covenant.core import TesseractCovenant

modulo = TesseractCovenant()

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
