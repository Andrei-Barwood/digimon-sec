
import sys
import os

# Aseguramos que podemos importar el módulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from manifold_fuzz.core import ManifoldFuzz

def main():
    print("🚀 Iniciando misión: Fleeting Joy")
    print("🛡️  Rol: Fuzz Tester")
    print("-" * 50)

    # 1. Inicialización
    print(f"\n[1] Inicializando ManifoldFuzz...")
    modulo = ManifoldFuzz(config={"mutation_rate": 0.2, "timeout_seconds": 1})
    
    # --- CONFIGURACIÓN DE FUZZING ---
    # Simulamos que estamos probando una función de login
    # Le damos un input base válido para que empiece a mutarlo
    base_input = "username=admin&password=secure123"
    iterations = 50
    
    print(f"🔨 Objetivo: Función de Login simulada")
    print(f"🧬 Input base: '{base_input}'")
    print(f"🔄 Iteraciones planificadas: {iterations}")
    # --------------------------------

    # 3. Ejecución de la Misión Principal
    print(f"[3] Ejecutando análisis de seguridad (Ejecuta fuzzing para encontrar bugs)...")
    result = modulo.analyze(base_input=base_input, iterations=iterations)

    # 4. Interpretación de Resultados
    print("\n[4] Informe de Misión:")
    print("-" * 30)
    print(f"Estado: {result.status.upper()}")
    print(f"Mensaje: {result.message}")
    
    if result.data:
        print("\n📊 RESULTADOS DEL FUZZING:")
        print(f"  - Tests ejecutados: {result.data.get('total_tests')}")
        print(f"  - Cobertura estimada: {result.data.get('coverage_percent'):.1f}%")
        
        crashes = result.data.get("crashes_found", 0)
        bugs = result.data.get("bugs_found", [])
        
        if crashes > 0:
            print(f"  💥 CRASHES: {crashes} (Crítico)")
            
        if bugs:
            print(f"\n🐛 BUGS ENCONTRADOS ({len(bugs)}):")
            for bug in bugs:
                print(f"  - {bug}")
        else:
            print("\n✅ El objetivo resistió el ataque (no se encontraron bugs obvios).")

    print("-" * 50)
    print("🏁 Misión cumplida.")

if __name__ == "__main__":
    main()
