# Arquitectura - lemniscate_mnemo

## Visión General

lemniscate_mnemo es un módulo de ciberseguridad implementado como parte del **Snocomm Security Suite**.

- **Misión**: Enter, Pursued by a Memory
- **Rol de Seguridad**: Backup Auditor
- **Nivel**: Production (v3.0.0)
- **Versión**: 3.0.0

## Propósito

Verifica integridad de backups, evalúa permisos y políticas de retención,
y apoya verificaciones de cifrado con algoritmos modernos.
Attributes:
name: Nombre del módulo
mission: Misión RDR2 inspiradora
role: Rol en ciberseguridad
hash_algorithm: Algoritmo de hash usado para checksum (default: sha512)
min_retention_days: Días mínimos de retención recomendados
check_encryption: Habilita avisos si el archivo parece sin cifrar
verify_permissions: Verifica permisos peligrosos (world-readable/writable)

## Estructura del Componente

### 1. Core Module (`core.py`)

La clase `LemniscateMnemo` es el punto de entrada principal. Implementa la lógica de negocio y orquesta las operaciones de seguridad.

**Responsabilidades:**
- `calculate_checksum()`: Calcular checksum seguro leyendo en chunks para minimizar memoria
- `verify_integrity()`: Verifica integridad y controles de superficie (permisos, cifrado indicativo)
- `audit_backup_directory()`: Audita un directorio de backups completo
- `check_retention_policy()`: Verifica cumplimiento de retención mínima
- `analyze()`: Ejecuta análisis principal: archivo individual o carpeta completa
- `validate()`: Valida rutas individuales o listas de rutas
- `get_info()`: Obtener información del módulo


### 2. Models (`models.py`)

Define la estructura de datos utilizando **Pydantic v2**, asegurando validación estricta y serialización segura.

**Modelos Principales:**
- `ModuleConfig`: Configuration model for LemniscateMnemo
- `BackupVerificationResult`: Result model for backup verification operations
- `AuditResult`: Result model for directory audit operations
- `AnalysisResult`: Result model for analysis operations
- `ModuleInfo`: Information model for módulo metadata


### 3. Utils (`utils.py`)

Proporciona utilidades auxiliares como configuración de logging y helpers comunes.

## Configuración y Personalización

El modulo se configura mediante un diccionario inmutable (`frozen=True` en Pydantic) pasado al inicializador.

```python
config = {
    "hash_algorithm": "sha512",  # Configura hash_algorithm
}
```

## Flujo de Trabajo Típico

1. **Inicialización**: Se carga la configuración y se validan las dependencias.
2. **Validación**: `validate()` verifica que los inputs cumplan los requisitos mínimos.
3. **Ejecución**: `analyze()` (u otros métodos específicos) procesa los datos aplicando la lógica de seguridad.
4. **Resultado**: Se retorna un objeto `AnalysisResult` estandarizado con estado, mensaje y datos.

## Estándares de Seguridad (2025-2026)

- **Validación de Tipos**: Uso extensivo de Type Hints y Pydantic.
- **Manejo de Errores Seguro**: Los errores se capturan y retornan estructurados, evitando crash no controlados.
- **Configuración Inmutable**: Previene modificaciones accidentales en tiempo de ejecución.

## Extensibilidad

Para agregar nuevas funcionalidades:
1. Definir nuevos modelos en `models.py`.
2. Implementar la lógica en `core.py`.
3. Agregar pruebas unitarias en `tests/test_core.py`.

---

Ver también: [README.md](../README.md), [USAGE.md](USAGE.md), [API.md](API.md)
