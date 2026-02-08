import sys
import os

# Aseguramos que podemos importar el modulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from geodesic_ledger.core import GeodesicLedger


def main():
    print("🚀 Iniciando mision: The Gilded Cage")
    print("🛡️  Rol: Cost Optimizer")
    print("-" * 50)

    print("\n[1] Inicializando GeodesicLedger...")
    modulo = GeodesicLedger()

    print("[2] Preparando datos...")
    cost_data = {
    "cost_anomalies": 0,
    "idle_resources": 0,
    "budget_guardrails": True,
}

    print("[3] Ejecutando analisis de seguridad...")
    result = modulo.analyze(cost_data=cost_data)

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
