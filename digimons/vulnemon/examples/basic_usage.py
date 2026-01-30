
import sys
import os

# Aseguramos que podemos importar el módulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from vulnemon.core import Vulnemon

def main():
    print("🚀 Iniciando misión: Paradise Mercifully Departed")
    print("🛡️  Rol: Vuln Scanner")
    print("-" * 50)

    # 1. Inicialización
    print(f"\n[1] Inicializando Vulnemon...")
    digimon = Vulnemon(config={"check_cves": True, "severity_threshold": "low"})
    
    # --- OBJETIVOS DE ESCANEO ---
    # Simulamos una lista de software instalado en un servidor
    targets = [
        "openssl-1.0.2",   # Vulnerable (Heartbleed/Certificate issues)
        "apache-2.4.41",   # Vulnerable (Log4j related if configured badly)
        "nginx-1.18.0",    # Seguro (en nuestra DB simulada)
        "python-3.9.5"     # Seguro
    ]
    print(f"🎯 Objetivos seleccionados: {', '.join(targets)}")
    # ----------------------------

    # 3. Ejecución de la Misión Principal
    print(f"[3] Ejecutando análisis de seguridad (Escanea vulnerabilidades conocidas)...")
    result = digimon.analyze(targets=targets)

    # 4. Interpretación de Resultados
    print("\n[4] Informe de Misión:")
    print("-" * 30)
    print(f"Estado: {result.status.upper()}")
    print(f"Mensaje: {result.message}")
    
    if result.data:
        print("\n🔍 HALLAZGOS DEL ESCANEO:")
        scans = result.data.get("scans", [])
        total_vulns = result.data.get("total_vulnerabilities", 0)
        
        if total_vulns == 0:
            print("  ✅ No se encontraron vulnerabilidades conocidas.")
        else:
            for scan in scans:
                vulns = scan.get("vulnerabilities", [])
                target_name = scan.get("scan_summary", {}).get("target")
                
                if vulns:
                    print(f"\n  🔴 {target_name}:")
                    for v in vulns:
                        print(f"     - [{v['cve_id']}] {v['severity'].upper()}: {v['description']}")
                        print(f"       Recomendación: {v['recommendation']}")
                else:
                    print(f"\n  🟢 {target_name}: Seguro")

    print("-" * 50)
    print("🏁 Misión cumplida.")

if __name__ == "__main__":
    main()
