import sys
import os

# Aseguramos que podemos importar el modulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from dockermon.core import Dockermon


def main():
    print("🚀 Iniciando mision: A Kind and benevolent Despot")
    print("🛡️  Rol: Docker Auditor")
    print("-" * 50)

    print("\n[1] Inicializando Dockermon...")
    digimon = Dockermon()

    print("[2] Preparando datos...")
    container_data = {
    "run_as_root": False,
    "privileged": False,
    "read_only_fs": True,
    "signed_images": True,
}

    print("[3] Ejecutando analisis de seguridad...")
    result = digimon.analyze(container_data=container_data)

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
