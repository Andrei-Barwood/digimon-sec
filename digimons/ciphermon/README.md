# 🎮 Ciphermon - Encryption Hero (Mega)

**Misión RDR2**: American Venom  
**Rol de Ciberseguridad**: encryption-expert  
**Estado**: 🟢 Mega (v3.0.0)  
**Mantenedor**: Kirtan Teg Singh  
**Licencia**: MIT

## 🎯 Propósito

Ciphermon valida políticas de cifrado modernas, detecta configuraciones débiles y ofrece utilidades seguras (generación de llaves, cifrado simulado con HMAC para integridad).

### Contexto Temático

En el universo de **DIGIMON CYBERSECURITY SUITE**, Ciphermon es el héroe del cifrado: aplica principios de “American Venom” para proteger el digimundo con criptografía sólida y controles de integridad.

## 🚀 Inicio Rápido

### Instalación

```bash
cd digimons/ciphermon
pip install -e .
```

### Uso Básico

```python
from ciphermon import Ciphermon

digimon = Ciphermon()

# Evaluar política
policy = digimon.analyze(cipher="AES-256-GCM", key_bits=256, aead=True)
print(policy)

# Cifrado simulado con integridad (HMAC)
enc = digimon.encrypt("hola digimundo")
print(enc)
dec = digimon.decrypt(enc.data["ciphertext"], enc.data["key"])
print(dec)
```

## ✨ Capacidades Mega (2025-2026)

- Políticas de cifrado con mínimos de keysize (256b por defecto)
- Requerir AEAD y alertar sobre ciphers legacy (DES/RC4/3DES/AES-128)
- Generación de llaves aleatorias seguras (base64 urlsafe)
- Cifrado simulado con HMAC-SHA256 para integridad
- Análisis unificado via `analyze` (policy + cifrado opcional)

## 📚 Documentación

- [Arquitectura](docs/ARCHITECTURE.md)
- [Guía de Uso](docs/USAGE.md)
- [API Reference](docs/API.md)
- [Instalación](docs/INSTALLATION.md)

## 🔄 Línea Evolutiva (Versioning)

| Fase | Versión | Características |
|------|---------|-----------------|
| 🔴 Rookie | 0.1.x | MVP básico |
| 🟠 Champion | 1.0.x | Integraciones API |
| 🟡 Ultimate | 2.0.x | Procesamiento avanzado |
| 🟢 Mega | 3.0.x | Políticas de cifrado y utilidades seguras |

## 🛠️ Desarrollo Local

```bash
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
pytest
```

## 📁 Estructura

```
ciphermon/
├── src/ciphermon/
│   ├── __init__.py
│   ├── core.py
│   ├── models.py
│   └── utils.py
├── tests/
│   └── test_core.py
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API.md
│   ├── USAGE.md
│   └── INSTALLATION.md
├── examples/  (opcional)
├── pyproject.toml
├── requirements.txt
└── README.md
```

## 📄 Licencia

MIT - ver [LICENSE](LICENSE)
# 🎮 ciphermon - Encryption Expert

**Misión RDR2**: American Venom  
**Rol de Ciberseguridad**: Encryption Expert  
**Estado**: Rookie (v0.1.0)  
**Mantenedor**: Kirtan Teg Singh  
**Licencia**: MIT

## 🎯 Propósito

Cifra tráfico con algoritmos avanzados

### Contexto Temático

En el universo de **DIGIMON CYBERSECURITY SUITE**, cada Digimon representa una especialidad de seguridad. ciphermon encarna los principios de la misión "American Venom" de Red Dead Redemption 2, aplicados al dominio cibernético.

## 🚀 Inicio Rápido

### Instalación

```bash
# Desde el repositorio principal
cd digimons/ciphermon
pip install -e .

# O instalación directa
pip install ciphermon
```

### Uso Básico

```python
from ciphermon import Ciphermon

# Crear instancia
digimon = Ciphermon()

# Usar funcionalidad principal
result = digimon.analyze()
print(result)
```

## 📚 Documentación

- [Arquitectura](docs/ARCHITECTURE.md) - Diseño técnico interno
- [Guía de Uso](docs/USAGE.md) - Ejemplos y patrones
- [API Reference](docs/API.md) - Documentación de funciones
- [Instalación](docs/INSTALLATION.md) - Pasos de setup

## 🔄 Línea Evolutiva (Versioning)

El desarrollo de ciphermon sigue la línea evolutiva de los Digimons:

| Fase | Versión | Características | Timeline |
|------|---------|-----------------|----------|
| 🔴 Rookie | 0.1.x | MVP básico, funcionalidad core | Actual |
| 🟠 Champion | 1.0.x | Integración con APIs, mejoras | Q2 2025 |
| 🟡 Ultimate | 2.0.x | Procesamiento avanzado, optimizaciones | Q3 2025 |
| 🟢 Mega | 3.0.x | Características AI/ML, distribución | Q4 2025 |

## 🛠️ Desarrollo Local

### Setup

```bash
# Clonar y navegar
cd digimons/ciphermon

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar en modo desarrollo
pip install -e ".[dev]"
```

### Testing

```bash
# Ejecutar todos los tests
pytest

# Con coverage
pytest --cov=ciphermon

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
ciphermon/
├── src/ciphermon/
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
**Status**: 🔴 Rookie Era (v0.1.0)
