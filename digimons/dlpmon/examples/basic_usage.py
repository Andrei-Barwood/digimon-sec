
import sys
import os

# Aseguramos que podemos importar el módulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from dlpmon.core import DLPmon

def main():
    print("🚀 Iniciando misión: The New Austin")
    print("🛡️  Rol: Data Loss Prevention")
    print("-" * 50)

    # 1. Inicialización
    print(f"\n[1] Inicializando DLPmon...")
    digimon = DLPmon(config={"sensitivity_level": "medium"})
    
    # --- MENSAJES SALIENTES SOSPECHOSOS ---
    # Simulamos una lista de mensajes que salen de la organización
    outgoing_messages = [
        "Hola equipo, ¿vamos a almorzar?",
        "Adjunto el reporte financiero Q3.",
        "Oye, mi clave temporal es Password123! para el servidor", # Violación potencial
        "El número de seguridad social del cliente es 123-45-6789" # Violación CRÍTICA
    ]
    print(f"📧 Escaneando {len(outgoing_messages)} mensajes salientes...")
    # ---------------------------------------

    # 3. Ejecución de la Misión Principal
    print(f"[3] Ejecutando análisis de seguridad (Previene fuga de datos sensibles)...")
    result = digimon.analyze(contents=outgoing_messages)

    # 4. Interpretación de Resultados
    print("\n[4] Informe de Misión:")
    print("-" * 30)
    print(f"Estado: {result.status.upper()}")
    print(f"Mensaje: {result.message}")
    
    if result.data:
        violations = result.data.get("violations", [])
        blocked = result.data.get("blocked_count", 0)
        
        if violations:
            print(f"\n🚨 {len(violations)} VIOLACIONES DETECTADAS:")
            for v in violations:
                severity = v.get('severity', 'unknown').upper()
                print(f"  - [{severity}] {v.get('policy_name')}: '{v.get('detected_data')}'")
        
        if blocked > 0:
            print(f"\n🛑 ACCIONES: {blocked} mensajes fueron BLOQUEADOS automáticamente.")
        else:
            print("\n✅ No se requirió bloqueo activo.")

    print("-" * 50)
    print("🏁 Misión cumplida.")

if __name__ == "__main__":
    main()
