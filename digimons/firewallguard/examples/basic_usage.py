import sys
import os

# Aseguramos que podemos importar el modulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from firewallguard.core import FirewallGuard


def main():
    print("🚀 Iniciando mision: Good, Honest Snake Oil")
    print("🛡️  Rol: Firewall Manager")
    print("-" * 50)

    print("\n[1] Inicializando FirewallGuard...")
    digimon = FirewallGuard()

    print("[2] Preparando datos de firewall...")
    rules_data = {
        "default_deny": True,
        "open_ports": [80, 443],
        "logging_enabled": True,
    }

    print("[3] Ejecutando analisis de seguridad...")
    result = digimon.analyze(rules_data=rules_data)

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

