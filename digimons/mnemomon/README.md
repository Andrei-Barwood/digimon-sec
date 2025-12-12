# 🎮 Mnemomon - Backup Auditor (Mega)

**Misión RDR2**: Enter, Pursued by a Memory  
**Rol de Ciberseguridad**: backup-auditor  
**Estado**: 🟢 Mega (v3.0.0)  
**Mantenedor**: Digimon Security Team  
**Licencia**: MIT

## 🎯 Propósito

Verifica integridad de backups, higiene de cifrado y cumplimiento de retención con prácticas de seguridad 2025-2026.

### Contexto Temático

En el universo de **DIGIMON CYBERSECURITY SUITE**, cada Digimon representa una especialidad de seguridad. Mnemomon encarna los principios de la misión "Enter, Pursued by a Memory" de Red Dead Redemption 2, aplicados al dominio cibernético de respaldo y continuidad.

## 🚀 Inicio Rápido

### Instalación

```bash
# Desde el repositorio principal
cd digimons/mnemomon
pip install -e .

# O instalación directa
pip install mnemomon
```

### Uso Básico (verificación puntual)

```python
from mnemomon import Mnemomon

digimon = Mnemomon()

# Verificar integridad de un backup con checksum esperado
result = digimon.analyze(
    backup_path="/path/to/backup.tar.gz",
    expected_checksum="abc123..."
)
print(result)
```

### Auditoría de carpeta completa

```python
from mnemomon import Mnemomon

digimon = Mnemomon(config={"min_retention_days": 30})

audit = digimon.analyze(directory_path="/backups/daily")
print(audit)
```

## ✨ Capacidades Mega (2025-2026)

- Hashing seguro (SHA-512 por defecto, SHA-256/BLAKE2 opcionales)
- Verificación de permisos (world-readable/writable) y alertas de cifrado
- Validación de políticas de retención con clasificación por edad
- Lectura en chunks (1MB) para archivos grandes
- Resultados tipados y aptos para CI
- Logging granular y mensajes accionables

## 📚 Documentación

- [Arquitectura](docs/ARCHITECTURE.md) - Diseño técnico interno
- [Guía de Uso](docs/USAGE.md) - Ejemplos y patrones
- [API Reference](docs/API.md) - Documentación de funciones
- [Instalación](docs/INSTALLATION.md) - Pasos de setup

## 🔄 Línea Evolutiva (Versioning)

| Fase | Versión | Características | Timeline |
|------|---------|-----------------|----------|
| 🔴 Rookie | 0.1.x | MVP básico, checksums locales | Pasado |
| 🟠 Champion | 1.0.x | Integración con APIs de backup | Pasado |
| 🟡 Ultimate | 2.0.x | Procesamiento avanzado | Pasado |
| 🟢 Mega | 3.0.x | Integridad, permisos, retención, cifrado | **Actual** |

## 🛠️ Desarrollo Local

### Setup

```bash
# Clonar y navegar
cd digimons/mnemomon

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\\Scripts\\activate

# Instalar en modo desarrollo
pip install -e ".[dev]"
```

### Testing

```bash
# Ejecutar todos los tests
pytest

# Con coverage
pytest --cov=Mnemomon

# Tests específicos
pytest tests/test_core.py -v
```

### Linting

```bash
black src/ tests/
flake8 src/ tests/
mypy src/
```

## 📁 Estructura del Proyecto

```
mnemomon/
├── src/mnemomon/
│   ├── __init__.py
│   ├── core.py              # Lógica principal
│   ├── models.py            # Modelos y tipos
│   ├── utils.py             # Utilidades
│   └── cli.py               # Interfaz CLI (opcional)
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   └── test_integration.py
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API.md
│   ├── USAGE.md
│   └── INSTALLATION.md
├── examples/
│   ├── basic_usage.py
│   └── demo.sh
├── pyproject.toml           # Configuración de proyecto
├── requirements.txt         # Dependencias
├── CHANGELOG.md             # Historial de versiones
├── LICENSE                  # Licencia
└── README.md                # Este archivo
```

## 🤝 Contribuir

Este proyecto es parte de [DIGIMON CYBERSECURITY SUITE](https://github.com/yourusername/digimon-sec-suite).

Por favor, consulta [CONTRIBUTING.md](../../CONTRIBUTING.md) para:
- Pautas de código
- Proceso de pull requests
- Líneas de evolución
- Estándares de documentación

## 📄 Licencia

MIT - Ver archivo [LICENSE](LICENSE)

## 🔗 Enlaces Útiles

- [DIGIMON CYBERSECURITY SUITE](https://github.com/yourusername/digimon-sec-suite)
- [Documentación Global](../../docs/)
- [Catálogo de Digimons](../../digimons/README_DIGIMONS.md)
- [Issues & Discussions](https://github.com/yourusername/digimon-sec-suite/issues)

---

**Última actualización**: 2025  
**Status**: 🟢 Mega Era (v3.0.0)
