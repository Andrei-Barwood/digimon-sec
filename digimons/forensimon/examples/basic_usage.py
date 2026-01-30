
import sys
import os

# Aseguramos que podemos importar el módulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from forensimon.core import Forensimon

def main():
    print("🚀 Iniciando misión: The New South")
    print("🛡️  Rol: Forensics Analyzer")
    print("-" * 50)

    # 1. Inicialización
    # Aquí es donde 'invocamos' a nuestro Digimon.
    print(f"\n[1] Inicializando Forensimon...")
    digimon = Forensimon()
    
    # --- CREACIÓN DE EVIDENCIA DE PRUEBA ---
    # Creamos un archivo de log falso para que Forensimon tenga algo que analizar
    sample_log = "suspicious_activity.log"
    with open(sample_log, "w") as f:
        f.write("2025-05-20 14:30:00 - User admin login from 192.168.1.50\n")
        f.write("2025-05-20 14:35:12 - API_KEY = 'secret_key_x89' exposed in logs\n")
        f.write("2025-05-20 14:36:00 - Failed password attempt for root\n")
    print(f"📄 Archivo de evidencia creado: {sample_log}")
    # ---------------------------------------

    # 2. Validación (Opcional)
    print("[2] Ejecutando diagnósticos internos...")
    if digimon.validate(sample_log):
         print("    ✅ Input válido")

    # 3. Ejecución de la Misión Principal
    # Pasamos el archivo que acabamos de crear
    print(f"[3] Ejecutando análisis de seguridad (Analiza logs y artifacts forenses)...")
    result = digimon.analyze(artifact_path=sample_log)

    # 4. Interpretación de Resultados
    print("\n[4] Informe de Misión:")
    print("-" * 30)
    print(f"Estado: {result.status.upper()}")
    print(f"Mensaje: {result.message}")
    
    if result.data:
        print("\nDatos Recolectados:")
        # Mostrar resumen si existe, o datos crudos
        summary = result.data.get("analysis_summary", {})
        if summary:
            print("  Resumen del Análisis:")
            for k, v in summary.items():
                print(f"   - {k}: {v}")
        
        # Mostrar IPs encontradas si las hay
        ips = result.data.get("ips_found", [])
        if ips:
            print(f"  IPs detectadas: {ips}")
            
        # Mostrar patrones sospechosos
        suspicious = result.data.get("suspicious_patterns", [])
        if suspicious:
             print(f"  ⚠️ Patrones sospechosos: {suspicious}")
    
    print("-" * 50)
    print("🏁 Misión cumplida.")
    
    # Limpieza
    if os.path.exists(sample_log):
        os.remove(sample_log)

if __name__ == "__main__":
    main()
