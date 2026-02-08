import sys
import os

# Aseguramos que podemos importar el modulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from vertex_stillness.core import VertexStillness


def main():
    print("🚀 Iniciando mision: Outlaws from the West")
    print("🛡️  Rol: VPC Monitor")
    print("-" * 50)

    print("\n[1] Inicializando VertexStillness...")
    modulo = VertexStillness()

    print("[2] Preparando datos de VPC...")
    vpc_data = {
        "flow_logs_enabled": True,
        "public_subnets": False,
        "network_acl_restrictive": True,
        "nat_gateway_configured": True,
    }

    print("[3] Ejecutando analisis de seguridad...")
    result = modulo.analyze(vpc_data=vpc_data)

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

