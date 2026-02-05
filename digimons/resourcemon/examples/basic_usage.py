import sys
import os

# Aseguramos que podemos importar el modulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from resourcemon.core import Resourcemon


def main():
    print("🚀 Iniciando mision: American Distillation")
    print("🛡️  Rol: Resource Limiter")
    print("-" * 50)

    print("\n[1] Inicializando Resourcemon...")
    digimon = Resourcemon()

    print("[2] Preparando datos...")
    usage_data = {
    "cpu_usage": 40,
    "memory_usage": 35,
    "storage_usage": 50,
}

    print("[3] Ejecutando analisis de seguridad...")
    result = digimon.analyze(usage_data=usage_data)

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
