#!/usr/bin/env python3
"""
Generador de Ejemplos Didácticos para Digimons.
Crea directorios 'examples/' con scripts funcionales y documentación amigable.
"""

import os
from pathlib import Path
import textwrap

# Base de datos de conocimientos (Blocks 1, 2, 3)
DIGIMON_DATA = {
    # Block 1: Offensive & Defense
    "thirstmon": {"mission": "Good, Honest Snake Oil", "role": "Threat Filter", "desc": "Filtra IoCs maliciosos, distingue amenazas reales"},
    "bandidmon": {"mission": "Outlaws from the West", "role": "Data Protector", "desc": "Protege datos en zonas fronterizas"},
    "mnemomon": {"mission": "Enter, Pursued by a Memory", "role": "Backup Auditor", "desc": "Verifica integridad de backups"},
    "ciphermon": {"mission": "American Venom", "role": "Encryption Expert", "desc": "Cifra/descifra tráfico con algoritmos avanzados"},
    "forensimon": {"mission": "The New South", "role": "Forensics Analyzer", "desc": "Analiza logs y artifacts forenses"},
    "networkmon": {"mission": "A Kind and benevolent Despot", "role": "Network Monitor", "desc": "Monitorea tráfico de red en tiempo real"},
    "vulnemon": {"mission": "Paradise Mercifully Departed", "role": "Vuln Scanner", "desc": "Escanea vulnerabilidades conocidas"},
    "logmon": {"mission": "Goodbye, Dear Friend", "role": "Log Analyzer", "desc": "Centraliza y analiza logs de seguridad"},
    "policymon": {"mission": "Charlotte Balfour", "role": "Policy Enforcer", "desc": "Valida cumplimiento de políticas de seguridad"},
    "incidentmon": {"mission": "The Gunslinger", "role": "Incident Response", "desc": "Automatiza respuesta a incidentes"},
    "fuzzymon": {"mission": "Fleeting Joy", "role": "Fuzz Tester", "desc": "Ejecuta fuzzing para encontrar bugs"},

    # Block 2: Identity & Access
    "identitymon": {"mission": "The Gunslinger", "role": "Identity Manager", "desc": "Gestiona identidades digitales"},
    "authmon": {"mission": "The Noblest of Men", "role": "Auth Handler", "desc": "Implementa autenticación multifactor"},
    "tokenmon": {"mission": "Red Dead Redemption", "role": "Token Manager", "desc": "Genera y valida tokens seguros"},
    "permissionmon": {"mission": "American Distillation", "role": "Permission Checker", "desc": "Valida permisos y accesos"},
    "credentialmon": {"mission": "Good Intentions", "role": "Credential Vault", "desc": "Almacena credenciales de forma segura"},
    "biometricmon": {"mission": "My Last Boy", "role": "Biometric Handler", "desc": "Procesa datos biométricos"},
    "sessionmon": {"mission": "Polite Society", "role": "Session Manager", "desc": "Gestiona sesiones de usuario"},
    "privilegemon": {"mission": "Clemens Point", "role": "Privilege Auditor", "desc": "Audita elevación de privilegios"},
    "passwordmon": {"mission": "The Gilded Cage", "role": "Password Validator", "desc": "Valida robustez de contraseñas"},
    "mfamon": {"mission": "Red Dead Redemption", "role": "MFA Enforcer", "desc": "Implementa autenticación multifactor"},
    "ldapmon": {"mission": "American Distillation", "role": "LDAP Manager", "desc": "Gestiona directorios LDAP"},
    "ssomon": {"mission": "Goodbye, Dear Friend", "role": "SSO Manager", "desc": "Implementa Single Sign-On"},
    "oauthmon": {"mission": "Marko Dragic", "role": "OAuth Handler", "desc": "Maneja flujos OAuth 2.0"},

    # Block 3: Data Protection
    "dlpmon": {"mission": "The New Austin", "role": "Data Loss Prevention", "desc": "Previene fuga de datos sensibles"},
    "redactionmon": {"mission": "Outlaws from the West", "role": "Data Redactor", "desc": "Redacta información PII automáticamente"},
    "anonymizemon": {"mission": "Charlotte Balfour", "role": "Anonymizer", "desc": "Anonimiza datos de test"},
    "encryptionmon": {"mission": "Forced Proximity", "role": "Encryption Manager", "desc": "Gestiona claves de cifrado"},
    "hashmon": {"mission": "Forever Yours, Arthur", "role": "Hash Validator", "desc": "Verifica integridad con hashes"},
    "maskingmon": {"mission": "Good, Honest Snake Oil", "role": "Data Masker", "desc": "Enmascara datos sensibles en logs"},
    "scrapingmon": {"mission": "All Debts Are Paid", "role": "Anti-Scraping Tool", "desc": "Previene web scraping"},
    "tokenizemon": {"mission": "Paradise Mercifully Departed", "role": "Tokenization Engine", "desc": "Tokeniza datos sensibles"},
    "compliancemon": {"mission": "Revenge", "role": "Compliance Checker", "desc": "Audita cumplimiento de regulaciones"},
    "gdprmon": {"mission": "Charlotte Balfour", "role": "GDPR Enforcer", "desc": "Cumple regulaciones GDPR"},
    "hipaamon": {"mission": "My Last Boy", "role": "HIPAA Auditor", "desc": "Valida cumplimiento HIPAA"},
    "pci-dssmon": {"mission": "The Gunslinger", "role": "PCI-DSS Validator", "desc": "Valida cumplimiento PCI-DSS"},
    "privacymon": {"mission": "Clemens Point", "role": "Privacy Auditor", "desc": "Audita políticas de privacidad"},
}

# Template para el script de Python (ejemplo funcional)
PYTHON_EXAMPLE_TEMPLATE = """
import sys
import os

# Aseguramos que podemos importar el módulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from {package_name}.core import {class_name}

def main():
    print("🚀 Iniciando misión: {mission}")
    print("🛡️  Rol: {role}")
    print("-" * 50)

    # 1. Inicialización
    # Aquí es donde 'invocamos' a nuestro Digimon.
    # Puedes pasar configuración personalizada si lo necesitas.
    print(f"\\n[1] Inicializando {name}...")
    digimon = {class_name}()
    
    # 2. Validación (Opcional pero recomendada)
    # Antes de lanzarnos a la acción, verificamos que todo esté en orden.
    print("[2] Ejecutando diagnósticos internos...")
    # data_to_validate = {{}} # Descomentar para validar datos específicos
    # if digimon.validate(data_to_validate):
    #     print("    ✅ Validación exitosa")

    # 3. Ejecución de la Misión Principal
    # Este es el momento de la verdad. Ejecutamos la lógica principal.
    print(f"[3] Ejecutando análisis de seguridad ({desc})...")
    result = digimon.analyze()

    # 4. Interpretación de Resultados
    print("\\n[4] Informe de Misión:")
    print("-" * 30)
    print(f"Estado: {{result.status.upper()}}")
    print(f"Mensaje: {{result.message}}")
    
    if result.data:
        print("\\nDatos Recolectados:")
        for key, value in result.data.items():
            print(f"  - {{key}}: {{value}}")
    
    print("-" * 50)
    print("🏁 Misión cumplida.")

if __name__ == "__main__":
    main()
"""

# Template para el README.md (Explicación didáctica)
README_EXAMPLE_TEMPLATE = """# 🎓 Ejemplos de Uso: {name}

¡Hola! Bienvenido al campo de entrenamiento de **{name}**.

Si estás aquí, es porque quieres ver a este Digimon en acción. Su misión, inspirada en *"{mission}"*, es clara: **{desc}**.

Aquí encontrarás ejemplos prácticos para entender cómo integrarlo en tus sistemas sin dolor de cabeza.

## 📂 Contenido

- `basic_usage.py`: Un script listo para ejecutar que demuestra el flujo básico de trabajo.

## 🚀 Cómo ejecutar el ejemplo

Es muy sencillo. Desde la raíz del proyecto (o desde este directorio), ejecuta:

```bash
python basic_usage.py
```

## 🧠 ¿Qué está pasando en el código?

El script `basic_usage.py` sigue un flujo lógico de 4 pasos que verás en casi todos nuestros Digimons:

1.  **Invocación**: Importamos e instanciamos la clase principal `{class_name}`. Es como sacar al Digimon de su Digivice.
2.  **Preparación**: (Opcional) Usamos `.validate()` para asegurarnos de que los datos de entrada (si los hay) son seguros y correctos.
3.  **Acción**: Llamamos a `.analyze()` (o métodos específicos como `.scan()`, `.encrypt()`). Aquí es donde ocurre la magia de seguridad.
4.  **Reporte**: Recibimos un objeto `AnalysisResult` estructurado. No más adivinar qué pasó; el Digimon te dice exactamente si hubo éxito, advertencia o error.

## 💡 Tips Pro

*   **Configuración**: La mayoría de estos Digimons aceptan un diccionario `config` al inicializarse. ¡No tengas miedo de personalizarlo! Revisa el archivo `USAGE.md` en el directorio padre para ver las opciones.
*   **Integración**: Este código está diseñado para ser copiado y pegado (con ligeros ajustes) en tus pipelines de CI/CD o scripts de automatización.

---
*"La seguridad no es un destino, es un viaje constante... y es mejor hacerlo acompañado de un buen Digimon."*
"""

def get_class_name_and_package(digimon_name, digimon_path):
    """
    Intenta adivinar el nombre de la clase y el paquete.
    Si falla la detección automática, hace un 'best guess'.
    """
    # Normalizar nombre de paquete (guiones a guiones bajos)
    package_name = digimon_name.replace("-", "_")
    
    # Intentar encontrar el nombre de la clase en el __init__.py o core.py
    # Por simplicidad y robustez, usaremos una heurística basada en capitalización
    # Ejemplo: pci-dssmon -> PCI_DSSmon, thirstmon -> Thirstmon
    
    if digimon_name == "pci-dssmon":
        class_name = "PCI_DSSmon"
    elif digimon_name == "scastmon": # Caso especial si existe
        class_name = "SCASTmon"
    else:
        # Capitalizar primera letra: thirstmon -> Thirstmon
        class_name = digimon_name.capitalize()
        # Casos especiales de nombres compuestos si los hubiera
    
    # Verificación real leyendo el archivo si es posible
    src_dir = digimon_path / "src"
    real_package_dir = None
    
    # Buscar directorio del paquete
    if (src_dir / package_name).exists():
        real_package_dir = src_dir / package_name
    elif (src_dir / digimon_name).exists():
        real_package_dir = src_dir / digimon_name
        package_name = digimon_name
    
    if real_package_dir:
        init_file = real_package_dir / "__init__.py"
        if init_file.exists():
            content = init_file.read_text()
            # Buscar "from .core import X"
            import re
            match = re.search(r'from \.core import (\w+)', content)
            if match:
                class_name = match.group(1)

    return class_name, package_name

def generate_example_docs():
    root_dir = Path(__file__).resolve().parent.parent
    digimons_dir = root_dir / "digimons"

    if not digimons_dir.exists():
        print("❌ No se encontró el directorio 'digimons'.")
        return

    count = 0
    print("🛠️  Generando ejemplos didácticos...")

    for digimon_dir in sorted(digimons_dir.iterdir()):
        if not digimon_dir.is_dir():
            continue
            
        name = digimon_dir.name
        
        # Verificar si tenemos datos para este digimon
        # Normalizamos a minúsculas para buscar en nuestro diccionario
        key = name.lower()
        
        if key not in DIGIMON_DATA:
            # Si no está en la lista explícita, usamos genéricos
            data = {
                "mission": "Protección del Digimundo", 
                "role": "Security Agent", 
                "desc": "Realiza operaciones de seguridad avanzadas"
            }
            # print(f"⚠️  Información genérica usada para {name}")
        else:
            data = DIGIMON_DATA[key]

        # Obtener nombres técnicos correctos
        class_name, package_name = get_class_name_and_package(name, digimon_dir)

        # Crear directorio examples
        examples_dir = digimon_dir / "examples"
        examples_dir.mkdir(exist_ok=True)

        # Generar basic_usage.py
        py_content = PYTHON_EXAMPLE_TEMPLATE.format(
            name=name.capitalize(),
            class_name=class_name,
            package_name=package_name,
            mission=data["mission"],
            role=data["role"],
            desc=data["desc"]
        ).strip()
        
        (examples_dir / "basic_usage.py").write_text(py_content, encoding='utf-8')

        # Generar README.md
        md_content = README_EXAMPLE_TEMPLATE.format(
            name=name.capitalize(),
            mission=data["mission"],
            desc=data["desc"],
            class_name=class_name
        ).strip()
        
        (examples_dir / "README.md").write_text(md_content, encoding='utf-8')
        
        print(f"✅ Ejemplos generados para {name} ({class_name})")
        count += 1

    print(f"\n✨ ¡Proceso completado! Se generó documentación didáctica para {count} digimons.")

if __name__ == "__main__":
    generate_example_docs()
