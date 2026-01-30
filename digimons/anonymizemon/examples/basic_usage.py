
import sys
import os

# Aseguramos que podemos importar el módulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from anonymizemon.core import Anonymizemon

def main():
    print("🚀 Iniciando misión: Charlotte Balfour")
    print("🛡️  Rol: Anonymizer")
    print("-" * 50)

    # 1. Inicialización
    print(f"\n[1] Inicializando Anonymizemon...")
    # Usamos pseudonimización reversible para pruebas
    digimon = Anonymizemon(config={
        "anonymization_method": "pseudonymize",
        "reversible": True
    })
    
    # --- DATOS DE USUARIO REALES (SIMULADOS) ---
    user_data = {
        "user_id": "12345",
        "full_name": "Arthur Morgan",
        "email": "arthur.m@gang.com",
        "age": "36",
        "role": "Enforcer"
    }
    print("👤 Datos originales:")
    for k, v in user_data.items():
        print(f"  {k}: {v}")
    # -------------------------------------------

    # 2. Validación
    print("\n[2] Validando estructura...")
    if digimon.validate(user_data):
        print("    ✅ Diccionario de datos válido")

    # 3. Ejecución de la Misión Principal
    print(f"[3] Ejecutando análisis de seguridad (Anonimiza datos de test)...")
    # Pasamos el diccionario de datos
    result = digimon.analyze(data=user_data)

    # 4. Interpretación de Resultados
    print("\n[4] Informe de Misión:")
    print("-" * 30)
    print(f"Estado: {result.status.upper()}")
    print(f"Mensaje: {result.message}")
    
    if result.data:
        print("\n🕵️  DATOS ANONIMIZADOS (Safe for Test):")
        anon_data = result.data.get("anonymized_data", {})
        for k, v in anon_data.items():
            print(f"  {k}: {v}")
            
        print(f"\nMétodo utilizado: {digimon.anonymization_method}")

    print("-" * 50)
    print("🏁 Misión cumplida.")

if __name__ == "__main__":
    main()
