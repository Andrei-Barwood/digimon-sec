import sys
import os

# Aseguramos que podemos importar el modulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from backupcloud.core import BackupCloud


def main():
    print("🚀 Iniciando mision: My Last Boy")
    print("🛡️  Rol: Cloud Backup Auditor")
    print("-" * 50)

    print("\n[1] Inicializando BackupCloud...")
    digimon = BackupCloud()

    print("[2] Preparando datos...")
    backup_data = {
    "backup_enabled": True,
    "backup_retention_days": 7,
    "last_backup_hours": 6,
    "cross_region_replication": True,
}

    print("[3] Ejecutando analisis de seguridad...")
    result = digimon.analyze(backup_data=backup_data)

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
