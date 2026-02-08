"""
Unit tests for HyperplaneCrawl (Production)
"""

import sys
from pathlib import Path

# Add src directory to Python path for local imports
# This ensures imports work both when running directly and with pytest
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import pytest

from hyperplane_crawl.core import HyperplaneCrawl
from hyperplane_crawl.models import AnalysisResult, ScrapingAttempt


@pytest.fixture
def modulo():
    """Fixture para crear instancia de HyperplaneCrawl"""
    return HyperplaneCrawl()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Hyperplane Crawl"
        assert modulo.mission == "All Debts Are Paid"
        assert modulo.role == "anti-scraping-tool"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"rate_limit_threshold": 50, "block_duration_minutes": 30}
        modulo = HyperplaneCrawl(config=config)
        assert modulo.rate_limit_threshold == 50
        assert modulo.block_duration_minutes == 30


class TestScrapingDetection:
    """Tests para detección de scraping"""

    def test_analyze_request_normal(self, modulo):
        """Test análisis de request normal"""
        attempt = modulo.analyze_request("192.168.1.1", "Mozilla/5.0")
        assert isinstance(attempt, ScrapingAttempt)
        assert attempt.severity in ["low", "medium", "high", "critical"]

    def test_analyze_request_suspicious_ua(self, modulo):
        """Test análisis de request con user agent sospechoso"""
        attempt = modulo.analyze_request("192.168.1.1", "bot/1.0")
        assert attempt.detection_method in ["user_agent", "none"]


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_requests(self, modulo):
        """Test analyze con lista de requests"""
        requests = [
            {"ip_address": "192.168.1.1", "user_agent": "Mozilla/5.0"},
            {"ip_address": "192.168.1.2", "user_agent": "bot/1.0"},
        ]
        result = modulo.analyze(requests=requests)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning", "error"]


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_requests(self, modulo):
        """Test validación con lista de requests válida"""
        requests = [{"ip_address": "192.168.1.1", "user_agent": "Mozilla/5.0"}]
        assert modulo.validate(requests) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Hyperplane Crawl"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

