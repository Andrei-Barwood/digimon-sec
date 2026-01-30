
import sys
import os

# Aseguramos que podemos importar el módulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from logmon.core import Logmon

def main():
    print("🚀 Iniciando misión: Goodbye, Dear Friend")
    print("🛡️  Rol: Log Analyzer")
    print("-" * 50)

    # 1. Inicialización
    print(f"\n[1] Inicializando Logmon...")
    digimon = Logmon()
    
    # --- CREACIÓN DE LOGS DE PRUEBA ---
    # Simulamos logs que contienen tráfico normal y algunos ataques
    sample_logs = [
        "2025-06-15 08:00:01 INFO Service started successfully",
        "2025-06-15 08:05:22 WARN High memory usage detected",
        "2025-06-15 09:12:00 ERROR Database connection failed",
        "2025-06-15 09:15:00 INFO User login: admin",
        "2025-06-15 10:00:00 ERROR Possible SQL Injection detected: SELECT * FROM users WHERE id='1' OR '1'='1'",
        "2025-06-15 10:01:00 ERROR XSS attempt blocked in /comment endpoint"
    ]
    print(f"📋 Cargando {len(sample_logs)} líneas de log simuladas...")
    # ----------------------------------

    # 2. Validación
    print("[2] Ejecutando diagnósticos internos...")
    if digimon.validate(sample_logs):
        print("    ✅ Formato de logs válido")

    # 3. Ejecución de la Misión Principal
    print(f"[3] Ejecutando análisis de seguridad (Centraliza y analiza logs de seguridad)...")
    # Pasamos la lista de logs directamente
    result = digimon.analyze(log_lines=sample_logs)

    # 4. Interpretación de Resultados
    print("\n[4] Informe de Misión:")
    print("-" * 30)
    print(f"Estado: {result.status.upper()}")
    print(f"Mensaje: {result.message}")
    
    if result.data:
        print("\nDatos Recolectados:")
        summary = result.data.get("analysis_summary", {})
        print(f"  - Total entradas: {summary.get('total_entries')}")
        print(f"  - Errores encontrados: {summary.get('error_count')}")
        print(f"  - Advertencias: {summary.get('warning_count')}")
        
        patterns = result.data.get("patterns_detected", [])
        if patterns:
            print(f"\n🚨 AMENAZAS DETECTADAS ({len(patterns)}):")
            for p in patterns:
                print(f"  - {p}")
    
    print("-" * 50)
    print("🏁 Misión cumplida.")

if __name__ == "__main__":
    main()
