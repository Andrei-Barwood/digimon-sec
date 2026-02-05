import sys
import os

# Aseguramos que podemos importar el modulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from terraformmon.core import Terraformmon


def main():
    print("🚀 Iniciando mision: Red Dead Redemption")
    print("🛡️  Rol: IaC Validator")
    print("-" * 50)

    print("\n[1] Inicializando Terraformmon...")
    digimon = Terraformmon()

    print("[2] Preparando datos...")
    iac_data = {
    "contains_hardcoded_secrets": False,
    "remote_state_encrypted": True,
    "plan_approved": True,
    "modules_pinned": True,
}

    print("[3] Ejecutando analisis de seguridad...")
    result = digimon.analyze(iac_data=iac_data)

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
