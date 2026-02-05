import sys
import os

# Aseguramos que podemos importar el modulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from compliancecloud.core import ComplianceCloud


def main():
    print("🚀 Iniciando mision: Good Intentions")
    print("🛡️  Rol: Cloud Compliance")
    print("-" * 50)

    print("\n[1] Inicializando ComplianceCloud...")
    digimon = ComplianceCloud()

    print("[2] Preparando datos...")
    compliance_data = {
    "passed_controls": 3,
    "evidence_collected": True,
    "continuous_monitoring": True,
    "frameworks_checked": ["SOC2"],
}

    print("[3] Ejecutando analisis de seguridad...")
    result = digimon.analyze(compliance_data=compliance_data)

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
