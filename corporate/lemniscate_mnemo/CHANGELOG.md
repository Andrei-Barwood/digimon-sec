# Changelog - LemniscateMnemo

## [3.0.0] - 2025-12-12 - 🟢 Production Era

### Added
- Hashing seguro por chunks con SHA-512 (default) y opciones SHA-256/BLAKE2
- Auditoría de permisos (world-readable/writable) y alertas de cifrado
- Verificación de políticas de retención con clasificación de backups viejos
- Modelos Pydantic para resultados tipados (`BackupVerificationResult`, `AuditResult`, `AnalysisResult`)
- Tests de integración puntual y de carpeta con fixtures temporales

### Changed
- Paquete publicado como `lemniscate_mnemo` (lowercase) para compatibilidad PyPI
- Rol normalizado a `backup-auditor` y estado Production en metadata

### Fixed
- Inconsistencias de import (LemniscateMnemo → lemniscate_mnemo) en docs y tests
- Mensajes de advertencia cuando no se provee checksum esperado

---

## [0.1.0] - 2025-01-15 - 🔴 Rookie Era

### Added
- Initial release
- Core LemniscateMnemo class
- Basic analysis functionality
- Data validation
- Logging utilities
- Comprehensive test suite
- Full documentation

### Features
- Verifica integridad de backups

---

## Línea Evolutiva (Versioning)

- 🔴 Rookie (v0.1.x) - MVP básico con funcionalidad core
- 🟠 Champion (v1.0.x) - Integraciones con APIs
- 🟡 Ultimate (v2.0.x) - Procesamiento avanzado
- 🟢 Production (v3.0.x) - Características AI/ML

---

[0.1.0]: https://github.com/snocomm-security/snocomm-security-suite/releases/tag/v0.1.0
