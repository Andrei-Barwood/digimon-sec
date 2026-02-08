import sys
import os

# Aseguramos que podemos importar el modulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from helix_vault.core import HelixVault


def main():
    print("🚀 Iniciando mision: The Noblest of Men")
    print("🛡️  Rol: Database Auditor")
    print("-" * 50)

    print("\n[1] Inicializando HelixVault...")
    modulo = HelixVault()

    print("[2] Preparando datos...")
    db_data = {
    "public_access": False,
    "storage_encrypted": True,
    "backup_retention_days": 7,
    "multi_az": True,
}

    print("[3] Ejecutando analisis de seguridad...")
    result = modulo.analyze(db_data=db_data)

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
