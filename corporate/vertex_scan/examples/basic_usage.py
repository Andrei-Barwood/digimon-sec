import sys
import os

# Aseguramos que podemos importar el módulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from Vertex Scan.core import VertexScan

def main():
    print("🚀 Iniciando misión: Protección del Digimundo")
    print("🛡️  Rol: Security Agent")
    print("-" * 50)

    # 1. Inicialización
    # Aquí es donde 'invocamos' a nuestro módulo.
    # Puedes pasar configuración personalizada si lo necesitas.
    print(f"\n[1] Inicializando VertexScan...")
    modulo = VertexScan()
    
    # 2. Validación (Opcional pero recomendada)
    # Antes de lanzarnos a la acción, verificamos que todo esté en orden.
    print("[2] Ejecutando diagnósticos internos...")
    # data_to_validate = {} # Descomentar para validar datos específicos
    # if modulo.validate(data_to_validate):
    #     print("    ✅ Validación exitosa")

    # 3. Ejecución de la Misión Principal
    # Este es el momento de la verdad. Ejecutamos la lógica principal.
    print(f"[3] Ejecutando análisis de seguridad (Realiza operaciones de seguridad avanzadas)...")
    result = modulo.analyze()

    # 4. Interpretación de Resultados
    print("\n[4] Informe de Misión:")
    print("-" * 30)
    print(f"Estado: {result.status.upper()}")
    print(f"Mensaje: {result.message}")
    
    if result.data:
        print("\nDatos Recolectados:")
        for key, value in result.data.items():
            print(f"  - {key}: {value}")
    
    print("-" * 50)
    print("🏁 Misión cumplida.")

if __name__ == "__main__":
    main()