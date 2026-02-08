import sys
import os

# Aseguramos que podemos importar el modulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from fractal_axiom.core import FractalAxiom


def main():
    print("🚀 Iniciando mision: American Venom")
    print("🛡️  Rol: Cloud Config Auditor")
    print("-" * 50)

    print("\n[1] Inicializando FractalAxiom...")
    modulo = FractalAxiom()

    print("[2] Preparando datos de configuracion...")
    config_data = {
        "encryption_enabled": True,
        "logging_enabled": True,
        "mfa_enabled": True,
        "public_access": False,
    }

    print("[3] Ejecutando analisis de seguridad...")
    result = modulo.analyze(config_data=config_data)

    print("\n[4] Informe de Mision:")
    print("-" * 30)
    print(f"Estado: {result.status.upper()}")
    print(f"Mensaje: {result.message}")
    if result.data:
        print("\nDatos Recolectados:")
        for key, value in result.data.items():
            print(f"  - {key}: {value}")
    print("-" * 50)
    print("🏁 Mision cumplida.")


if __name__ == "__main__":
    main()

