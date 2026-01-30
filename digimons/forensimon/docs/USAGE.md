# Guía de Uso - forensimon

## Inicio Rápido

### Instalación

```bash
pip install -e .
```

### Uso Básico

```python
from forensimon.core import Forensimon

# Crear instancia
digimon = Forensimon()

# Ejecutar análisis principal
# Forensimon requiere la ruta de un archivo (log, txt, etc.) para analizar
result = digimon.analyze(artifact_path="/var/log/syslog")
print(result)
```

## Configuración Avanzada

Puede configurar forensimon pasando un diccionario al constructor:

```python
digimon = Forensimon(config={
    "supported_formats": [".log", ".txt", ".json", ".csv", ".xml"],  # Configura supported_formats
    "extract_ips": True,
    "max_file_size_mb": 200
})
```

## Ejemplos de Uso

### Análisis Completo

Este ejemplo muestra cómo analizar un archivo de log específico, manejando la respuesta estructurada.

```python
import os
from forensimon.core import Forensimon

# 1. Preparación: Creamos un archivo de log de ejemplo (para demostración)
sample_log = "security_audit.log"
with open(sample_log, "w") as f:
    f.write("2025-05-20 14:30:00 - User admin login from 192.168.1.50\n")
    f.write("2025-05-20 14:35:12 - Failed password attempt for root\n")

# 2. Inicialización
digimon = Forensimon()

# 3. Ejecución del análisis
# Pasamos la ruta del archivo que queremos inspeccionar
print(f"Analizando {sample_log}...")
result = digimon.analyze(artifact_path=sample_log)

# 4. Procesamiento de resultados
if result.status == "success":
    print(f"✅ Operación exitosa: {result.message}")
    
    # Acceder a los datos específicos de forensimon
    analysis = result.data
    print(f"  - Líneas analizadas: {analysis.get('line_count')}")
    print(f"  - IPs encontradas: {analysis.get('ips_found')}")
    print(f"  - Patrones sospechosos: {analysis.get('suspicious_patterns')}")

elif result.status == "warning":
    print(f"⚠️ Advertencia: {result.message}")
else:
    print(f"❌ Error: {result.message}")
    print("Errores:", result.errors)

# Limpieza (opcional)
if os.path.exists(sample_log):
    os.remove(sample_log)
```

### Validación de Datos

```python
data = "ruta/al/archivo.log" # Datos a validar (Forensimon valida que el input sea string válido)
if digimon.validate(data):
    print("Input válido para procesar")
else:
    print("Input inválido")
```

## Mejores Prácticas (2025-2026)

1. **Configuración Mínima**: Comience con la configuración por defecto y ajuste según necesidad.
2. **Manejo de Errores**: Verifique siempre `result.status` antes de procesar `result.data`.
3. **Logs**: Configure el nivel de logging adecuado para producción vs desarrollo.
4. **Validación**: Use el método `validate()` antes de procesar datos externos no confiables.

---

Ver también: [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md)
