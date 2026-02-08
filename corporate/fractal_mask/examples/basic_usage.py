
import sys
import os

# Aseguramos que podemos importar el módulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from fractal_mask.core import FractalMask

def main():
    print("🚀 Iniciando misión: Good, Honest Snake Oil")
    print("🛡️  Rol: Data Masker")
    print("-" * 50)

    # 1. Inicialización
    print(f"\n[1] Inicializando FractalMask...")
    # Preservar formato ayuda a que los logs sigan siendo legibles/parseables
    modulo = FractalMask(config={"preserve_format": True})
    
    # --- LOG SIN PROCESAR ---
    raw_log = (
        "INFO: Payment processed for card 4111-1111-1111-1234 successfully.\n"
        "DEBUG: User phone verified: (555) 123-4567.\n"
        "WARN: Connection from IP 203.0.113.45 attempted admin access."
    )
    print("📜 Log original (Raw):")
    print(raw_log)
    print("-" * 20)
    # ------------------------

    # 3. Ejecución de la Misión Principal
    print(f"[3] Ejecutando análisis de seguridad (Enmascara datos sensibles en logs)...")
    result = modulo.analyze(text=raw_log)

    # 4. Interpretación de Resultados
    print("\n[4] Informe de Misión:")
    print("-" * 30)
    print(f"Estado: {result.status.upper()}")
    print(f"Mensaje: {result.message}")
    
    if result.data:
        print("\n🎭 LOG ENMASCARADO (Seguro para almacenamiento):")
        print(">" * 20)
        print(result.data.get("masked_text"))
        print("<" * 20)
        
        print(f"\nItems enmascarados: {result.data.get('total_masked')}")

    print("-" * 50)
    print("🏁 Misión cumplida.")

if __name__ == "__main__":
    main()
