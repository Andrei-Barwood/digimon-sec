
import sys
import os

# Aseguramos que podemos importar el módulo localmente para pruebas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from hyperplane_crawl.core import HyperplaneCrawl

def main():
    print("🚀 Iniciando misión: All Debts Are Paid")
    print("🛡️  Rol: Anti-Scraping Tool")
    print("-" * 50)

    # 1. Inicialización
    print(f"\n[1] Inicializando HyperplaneCrawl...")
    # Configuramos rate limit bajo para demostrar bloqueo fácil
    modulo = HyperplaneCrawl(config={"rate_limit_threshold": 5, "block_duration_minutes": 10})
    
    # --- TRÁFICO WEB SIMULADO (SCRAPING ATTACK) ---
    attacker_ip = "10.0.0.66"
    bot_agent = "SuperBot/1.0 (Crawler)"
    
    # Generamos ráfaga de requests del atacante
    requests = []
    # 10 peticiones rápidas del bot
    for _ in range(10):
        requests.append({"ip_address": attacker_ip, "user_agent": bot_agent})
    
    # Y una petición de un usuario normal
    requests.append({"ip_address": "192.168.1.5", "user_agent": "Mozilla/5.0 (Windows NT 10.0)"})
    
    print(f"🕸️  Analizando ráfaga de {len(requests)} peticiones...")
    # ----------------------------------------------

    # 3. Ejecución de la Misión Principal
    print(f"[3] Ejecutando análisis de seguridad (Previene web scraping)...")
    result = modulo.analyze(requests=requests)

    # 4. Interpretación de Resultados
    print("\n[4] Informe de Misión:")
    print("-" * 30)
    print(f"Estado: {result.status.upper()}")
    print(f"Mensaje: {result.message}")
    
    if result.data:
        stats = result.data.get("attempts_by_method", {})
        print("\nDetecciones por método:")
        for metodo, cantidad in stats.items():
            print(f"  - {metodo}: {cantidad}")
            
        blocked = result.data.get("blocked_attempts", 0)
        print(f"\n🚫 Peticiones BLOQUEADAS: {blocked}")
        
        # Mostrar detalle de bloqueo
        attempts = result.data.get("attempts", [])
        blocked_attempts = [a for a in attempts if a['blocked']]
        if blocked_attempts:
            example = blocked_attempts[0]
            print(f"  Ejemplo de bloqueo: IP {example['ip_address']} detectada por '{example['detection_method']}'")

    print("-" * 50)
    print("🏁 Misión cumplida.")

if __name__ == "__main__":
    main()
