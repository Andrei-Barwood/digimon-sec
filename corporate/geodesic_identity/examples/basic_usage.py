import sys
import os

# Aseguramos que podemos importar el modulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from geodesic_identity.core import GeodesicIdentity


def main():
    print("🚀 Iniciando mision: Charlotte Balfour")
    print("🛡️  Rol: IAM Analyzer")
    print("-" * 50)

    print("\n[1] Inicializando GeodesicIdentity...")
    modulo = GeodesicIdentity()

    print("[2] Preparando datos IAM...")
    iam_data = {
        "wildcard_permissions": False,
        "mfa_enforced": True,
        "rotation_enabled": True,
        "inactive_users": 0,
    }

    print("[3] Ejecutando analisis de seguridad...")
    result = modulo.analyze(iam_data=iam_data)

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

