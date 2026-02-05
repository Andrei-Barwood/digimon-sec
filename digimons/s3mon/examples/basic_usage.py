import sys
import os

# Aseguramos que podemos importar el modulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from s3mon.core import S3mon


def main():
    print("🚀 Iniciando mision: Paradise Mercifully Departed")
    print("🛡️  Rol: S3 Auditor")
    print("-" * 50)

    print("\n[1] Inicializando S3mon...")
    digimon = S3mon()

    print("[2] Preparando datos de bucket...")
    bucket_data = {
        "public_access": False,
        "encryption_enabled": True,
        "versioning_enabled": True,
        "logging_enabled": True,
    }

    print("[3] Ejecutando analisis de seguridad...")
    result = digimon.analyze(bucket_data=bucket_data)

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

