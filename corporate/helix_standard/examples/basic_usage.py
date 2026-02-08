
import sys
import os

# Aseguramos que podemos importar el módulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from helix_standard.core import HelixStandard

def main():
    print("🚀 Iniciando misión: The Gunslinger")
    print("🛡️  Rol: PCI-DSS Validator")
    print("-" * 50)

    # 1. Inicialización
    print(f"\n[1] Inicializando PCI-DSSmon...")
    # Podemos configurar modo estricto o relajado
    modulo = HelixStandard(config={"strict_mode": False})
    
    # --- SIMULACIÓN DE SISTEMA A AUDITAR ---
    # Definimos las características de seguridad de nuestro "sistema objetivo"
    target_system = {
        "name": "PaymentGateway_v1",
        "card_data_encryption": True,        # Cumple Req 3.4
        "transmission_encryption": True,     # Cumple Req 4.1
        "network_segmentation": True,        # Buena práctica
        "access_controls_enabled": True,     # Cumple Req 7.1
        "vulnerability_scanning": False,     # FALLO: No tiene escaneo (Req 6.1)
        "network_monitoring": False          # FALLO: No monitoreado (Req 10.1)
    }
    print(f"🏢 Sistema objetivo: {target_system['name']}")
    print("   (Simulando auditoría de cumplimiento...)")
    # ---------------------------------------

    # 2. Validación
    print("[2] Validando datos del objetivo...")
    if modulo.validate(target_system):
        print("    ✅ Datos estructuralmente válidos")

    # 3. Ejecución de la Misión Principal
    print(f"[3] Ejecutando análisis de seguridad (Valida cumplimiento PCI-DSS)...")
    result = modulo.analyze(target_data=target_system)

    # 4. Interpretación de Resultados
    print("\n[4] Informe de Misión:")
    print("-" * 30)
    print(f"Estado: {result.status.upper()}")
    print(f"Mensaje: {result.message}")
    
    if result.data:
        print("\nDetalles de Cumplimiento:")
        score = result.data.get("compliance_score", 0)
        passed = result.data.get("passed_checks", 0)
        failed = result.data.get("failed_checks", 0)
        
        print(f"  📊 Puntaje Global: {score:.1f}%")
        print(f"  ✅ Controles Aprobados: {passed}")
        print(f"  ❌ Controles Fallidos: {failed}")
        
        checks = result.data.get("checks", [])
        failures = [c for c in checks if c["status"] == "fail"]
        
        if failures:
            print("\n🚨 RECOMENDACIONES DE REMEDIACIÓN:")
            for fail in failures:
                print(f"  - [{fail['requirement']}] {fail['description']}")
                print(f"    Solución: {fail['remediation']}")

    print("-" * 50)
    print("🏁 Misión cumplida.")

if __name__ == "__main__":
    main()
