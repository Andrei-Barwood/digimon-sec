
import sys
import os

# Aseguramos que podemos importar el módulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from redactionmon.core import Redactionmon

def main():
    print("🚀 Iniciando misión: Outlaws from the West")
    print("🛡️  Rol: Data Redactor")
    print("-" * 50)

    # 1. Inicialización
    print(f"\n[1] Inicializando Redactionmon...")
    # Configuramos el estilo de redacción
    digimon = Redactionmon(config={"redaction_style": "mask"})
    
    # --- TEXTO CON INFORMACIÓN SENSIBLE ---
    sensitive_text = (
        "Reporte de Incidente #90210\n"
        "El usuario John Doe (j.doe@example.corp) intentó acceder.\n"
        "Teléfono de contacto: 555-0199-8822\n"
        "IP origen: 192.168.1.45\n"
        "Tarjeta usada: 4532-1234-5678-9012"
    )
    print("📄 Texto original con PII:")
    print("-" * 20)
    print(sensitive_text)
    print("-" * 20)
    # --------------------------------------

    # 2. Validación
    print("\n[2] Validando input...")
    if digimon.validate(sensitive_text):
        print("    ✅ Texto válido para procesamiento")

    # 3. Ejecución de la Misión Principal
    print(f"[3] Ejecutando análisis de seguridad (Redacta información PII automáticamente)...")
    result = digimon.analyze(text=sensitive_text)

    # 4. Interpretación de Resultados
    print("\n[4] Informe de Misión:")
    print("-" * 30)
    print(f"Estado: {result.status.upper()}")
    print(f"Mensaje: {result.message}")
    
    if result.data:
        print("\n📝 TEXTO REDACTADO:")
        print(">" * 20)
        print(result.data.get("redacted_text"))
        print("<" * 20)
        
        stats = result.data.get("redactions_by_type", {})
        if stats:
            print(f"\nEstadísticas de censura:")
            for tipo, cantidad in stats.items():
                print(f"  - {tipo}: {cantidad} ocurrencias")

    print("-" * 50)
    print("🏁 Misión cumplida.")

if __name__ == "__main__":
    main()
