#!/bin/bash

################################################################################
# Snocomm Security Suite - Test Runner
# Ejecuta pytest en todos los módulos y muestra estadísticas
################################################################################

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Contadores
total_corporate=0
passed_corporate=0
failed_corporate=0

echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo -e "${BLUE}    🧪 TESTING ALL MODULES - Snocomm Security Suite${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo ""

# Navegar al directorio base del proyecto (donde está tools/)
cd "$(dirname "$0")/.." || exit 1

# Verificar si existe la carpeta corporate
if [ ! -d "corporate" ]; then
    echo -e "${RED}❌ Error: No se encuentra la carpeta 'corporate'${NC}"
    echo "Ejecuta este script desde la raíz del proyecto."
    exit 1
fi

# Iterar sobre cada módulo
for modulo_dir in corporate/*/; do
    # Extraer nombre del módulo
    modulo_name=$(basename "$modulo_dir")
    
    # Verificar que tiene tests
    if [ ! -d "$modulo_dir/tests" ]; then
        echo -e "${YELLOW}⚠️  $modulo_name - No tiene carpeta tests, saltando...${NC}"
        continue
    fi
    
    total_corporate=$((total_corporate + 1))
    
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "📦 Testing: ${YELLOW}$modulo_name${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    
    # Cambiar al directorio del módulo
    cd "$modulo_dir" || continue
    
    # Ejecutar pytest (silenciar output detallado, solo mostrar resumen)
    if pytest -q --tb=short 2>&1; then
        echo -e "${GREEN}✅ $modulo_name PASSED${NC}"
        passed_corporate=$((passed_corporate + 1))
    else
        echo -e "${RED}❌ $modulo_name FAILED${NC}"
        failed_corporate=$((failed_corporate + 1))
    fi
    
    # Volver al directorio raíz
    cd - > /dev/null || exit 1
    echo ""
done


# Tests de integración
if [ -f "tests/test_integration.py" ]; then
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "🔗 Testing: ${YELLOW}Integration Tests${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    
    if pytest tests/test_integration.py -q --tb=short 2>&1; then
        echo -e "${GREEN}✅ Integration Tests PASSED${NC}"
    else
        echo -e "${RED}❌ Integration Tests FAILED${NC}"
    fi
    echo ""
fi


# Mostrar resumen final
echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo -e "${BLUE}              📊 RESUMEN DE TESTS${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo -e "Total módulos testeados: ${YELLOW}$total_corporate${NC}"
echo -e "Pasaron correctamente:    ${GREEN}$passed_corporate${NC}"
echo -e "Fallaron:                 ${RED}$failed_corporate${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"

# Exit code basado en resultados
if [ $failed_corporate -eq 0 ] && [ $total_corporate -gt 0 ]; then
    echo -e "${GREEN}🎉 ¡Todos los tests pasaron exitosamente!${NC}"
    exit 0
elif [ $total_corporate -eq 0 ]; then
    echo -e "${YELLOW}⚠️  No se encontraron módulos para testear${NC}"
    exit 1
else
    echo -e "${RED}💥 Algunos tests fallaron. Revisa los errores arriba.${NC}"
    exit 1
fi
