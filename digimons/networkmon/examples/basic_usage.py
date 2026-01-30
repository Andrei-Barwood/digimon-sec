
import sys
import os

# Aseguramos que podemos importar el módulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from networkmon.core import Networkmon

def main():
    print("🚀 Iniciando misión: A Kind and benevolent Despot")
    print("🛡️  Rol: Network Monitor")
    print("-" * 50)

    # 1. Inicialización
    print(f"\n[1] Inicializando Networkmon...")
    digimon = Networkmon(config={"alert_threshold": 5}) # Umbral bajo para forzar alertas en demo
    
    # --- TRÁFICO DE RED SIMULADO ---
    traffic_batch = [
        {"source_ip": "192.168.1.10", "dest_ip": "8.8.8.8", "dest_port": 53, "protocol": "UDP"},     # DNS (Normal)
        {"source_ip": "192.168.1.10", "dest_ip": "104.21.55.2", "dest_port": 443, "protocol": "TCP"}, # HTTPS (Normal)
        {"source_ip": "192.168.1.10", "dest_ip": "104.21.55.2", "dest_port": 443, "protocol": "TCP"},
        {"source_ip": "45.33.22.11", "dest_ip": "192.168.1.5", "dest_port": 22, "protocol": "TCP"},  # SSH (Sospechoso si es externo)
        {"source_ip": "45.33.22.11", "dest_ip": "192.168.1.5", "dest_port": 22, "protocol": "TCP"},  # Fuerza bruta SSH?
        {"source_ip": "45.33.22.11", "dest_ip": "192.168.1.5", "dest_port": 3389, "protocol": "TCP"} # RDP (Muy sospechoso)
    ]
    print(f"📡 Inyectando {len(traffic_batch)} paquetes de tráfico simulado...")
    # -------------------------------

    # 3. Ejecución de la Misión Principal
    print(f"[3] Ejecutando análisis de seguridad (Monitorea tráfico de red en tiempo real)...")
    # Pasamos el lote de conexiones
    result = digimon.analyze(connections=traffic_batch)

    # 4. Interpretación de Resultados
    print("\n[4] Informe de Misión:")
    print("-" * 30)
    print(f"Estado: {result.status.upper()}")
    print(f"Mensaje: {result.message}")
    
    if result.data:
        print("\n📊 ANÁLISIS DE TRÁFICO:")
        summary = result.data.get("analysis_summary", {})
        
        print(f"  - IPs Únicas: {summary.get('unique_ip_count')}")
        print(f"  - Puerto más usado: {summary.get('most_used_port')}")
        print(f"  - Protocolo dominante: {summary.get('most_used_protocol')}")
        
        suspicious = result.data.get("suspicious_connections", [])
        if suspicious:
            print(f"\n⚠️  CONEXIONES SOSPECHOSAS DETECTADAS ({len(suspicious)}):")
            for conn in suspicious:
                print(f"  - {conn.get('source_ip')} -> {conn.get('dest_ip')}:{conn.get('dest_port')} ({conn.get('protocol')})")

        alerts = summary.get("alerts", [])
        if alerts:
            print(f"\n🔔 ALERTAS ACTIVAS:")
            for alert in alerts:
                print(f"  - {alert}")

    print("-" * 50)
    print("🏁 Misión cumplida.")

if __name__ == "__main__":
    main()
