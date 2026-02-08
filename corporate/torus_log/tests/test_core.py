"""
Unit tests for TorusLog (Production)
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

from torus_log.core import TorusLog
from torus_log.models import AnalysisResult, LogAnalysis


@pytest.fixture
def modulo():
    """Fixture para crear instancia de TorusLog"""
    return TorusLog()


class TestInitialization:
    """Tests para inicialización"""

    def test_init_default(self, modulo):
        """Test inicialización con valores por defecto"""
        assert modulo.name == "Torus Log"
        assert modulo.mission == "Goodbye, Dear Friend"
        assert modulo.role == "log-analyzer"

    def test_init_with_config(self):
        """Test inicialización con configuración"""
        config = {"log_levels": ["ERROR", "WARN"], "correlation_window": 600}
        modulo = TorusLog(config=config)
        assert len(modulo.log_levels) == 2
        assert modulo.correlation_window == 600


class TestLogParsing:
    """Tests para parsing de logs"""

    def test_parse_log_entry(self, modulo):
        """Test parsear entrada de log"""
        log_line = "2025-01-15 10:30:45 ERROR Connection failed"
        entry = modulo.parse_log_entry(log_line)
        assert entry is not None
        assert entry.level == "ERROR"

    def test_analyze_logs(self, modulo):
        """Test análisis de logs"""
        log_lines = [
            "2025-01-15 10:30:45 ERROR Connection failed",
            "2025-01-15 10:31:00 WARN High memory usage",
        ]
        analysis = modulo.analyze_logs(log_lines)
        assert isinstance(analysis, LogAnalysis)
        assert analysis.total_entries == 2


class TestAnalyze:
    """Tests para funcionalidad de análisis"""

    def test_analyze_with_string(self, modulo):
        """Test analyze con string"""
        log_data = "2025-01-15 10:30:45 ERROR Connection failed\n2025-01-15 10:31:00 INFO Operation completed"
        result = modulo.analyze(log_data=log_data)
        assert isinstance(result, AnalysisResult)
        assert result.status in ["success", "warning"]

    def test_analyze_with_list(self, modulo):
        """Test analyze con lista"""
        log_lines = ["2025-01-15 10:30:45 ERROR Connection failed"]
        result = modulo.analyze(log_lines=log_lines)
        assert isinstance(result, AnalysisResult)

    def test_analyze_no_input(self, modulo):
        """Test analyze sin input"""
        result = modulo.analyze()
        assert result.status == "error"


class TestValidation:
    """Tests para validación"""

    def test_validate_none(self, modulo):
        """Test validación con None"""
        assert modulo.validate(None) is False

    def test_validate_str(self, modulo):
        """Test validación con string"""
        assert modulo.validate("log line") is True

    def test_validate_list(self, modulo):
        """Test validación con lista"""
        assert modulo.validate(["log1", "log2"]) is True


class TestInfo:
    """Tests para información del módulo"""

    def test_get_info_returns_dict(self, modulo):
        """Test que get_info() retorna diccionario"""
        info = modulo.get_info()
        assert isinstance(info, dict)
        assert info["name"] == "Torus Log"
        assert info["status"] == "Production"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
