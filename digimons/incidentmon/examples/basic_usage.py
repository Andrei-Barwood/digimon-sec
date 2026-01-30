
import sys
import os

# Aseguramos que podemos importar el módulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from incidentmon.core import Incidentmon

def main():
    print("🚀 Iniciando misión: The Gunslinger")
    print("🛡️  Rol: Incident Response")
    print("-" * 50)

    # 1. Inicialización
    print(f"\n[1] Inicializando Incidentmon...")
    # Habilitamos contención automática para incidentes graves
    digimon = Incidentmon(config={"auto_contain": True, "notification_enabled": True})
    
    # --- FLUJO DE INCIDENTES ENTRANTES ---
    incidents = [
        {
            "incident_type": "malware_detected",
            "severity": "critical",
            "target": "server-production-01",
            "description": "Ransomware signature detected in /var/www"
        },
        {
            "incident_type": "failed_login",
            "severity": "low",
            "target": "workstation-hr-04",
            "description": "User mistyped password 3 times"
        }
    ]
    print(f"🚨 Procesando {len(incidents)} incidentes de seguridad reportados...")
    # -------------------------------------

    # 3. Ejecución de la Misión Principal
    print(f"[3] Ejecutando análisis de seguridad (Automatiza respuesta a incidentes)...")
    result = digimon.analyze(incidents=incidents)

    # 4. Interpretación de Resultados
    print("\n[4] Informe de Misión:")
    print("-" * 30)
    print(f"Estado: {result.status.upper()}")
    print(f"Mensaje: {result.message}")
    
    if result.data:
        responses = result.data.get("responses", [])
        
        print("\nACCIONES TOMADAS:")
        for resp in responses:
            summary = resp.get("response_summary", {})
            target = summary.get("target")
            severity = resp.get("severity", "unknown").upper()
            status = resp.get("status").upper()
            
            print(f"\n🔴 Incidente en {target} [{severity}]:")
            print(f"   Estado Final: {status}")
            
            actions = resp.get("actions_taken", [])
            if actions:
                for action in actions:
                    print(f"   ⚡ Acción ejecutada: {action['action_type'].upper()} -> {action['status']}")
            else:
                print("   ℹ️  Sin acciones automáticas (Solo monitoreo)")

    print("-" * 50)
    print("🏁 Misión cumplida.")

if __name__ == "__main__":
    main()
