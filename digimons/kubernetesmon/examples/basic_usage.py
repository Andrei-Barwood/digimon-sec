import sys
import os

# Aseguramos que podemos importar el modulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from kubernetesmon.core import Kubernetesmon


def main():
    print("🚀 Iniciando mision: Fleeting Joy")
    print("🛡️  Rol: K8s Scanner")
    print("-" * 50)

    print("\n[1] Inicializando Kubernetesmon...")
    digimon = Kubernetesmon()

    print("[2] Preparando datos...")
    cluster_data = {
    "rbac_enabled": True,
    "pod_security_policies": True,
    "etcd_encryption": True,
    "public_api": False,
}

    print("[3] Ejecutando analisis de seguridad...")
    result = digimon.analyze(cluster_data=cluster_data)

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
