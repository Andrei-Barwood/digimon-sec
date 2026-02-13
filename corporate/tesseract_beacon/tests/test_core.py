"""
Unit tests for TesseractBeacon (Production)
"""

import pytest

from tesseract_beacon.core import TesseractBeacon
from tesseract_beacon.models import AnalysisResult, DetectionReport


@pytest.fixture
def module():
    return TesseractBeacon()


def test_init_default(module):
    assert module.name == "Tesseract Beacon"
    assert module.mission == "Polite Society"
    assert module.role == "threatintel-aggregator"


def test_primary_method(module):
    data = {
    "feed_count": 12,
    "ioc_overlap_ratio": 0.67,
    "stale_feed_detected": False,
    "high_confidence_iocs": 28,
}
    report = module.aggregate_threat_intel(data)
    assert isinstance(report, DetectionReport)
    assert report.total_checks > 0


def test_analyze(module):
    data = {
    "feed_count": 12,
    "ioc_overlap_ratio": 0.67,
    "stale_feed_detected": False,
    "high_confidence_iocs": 28,
}
    result = module.analyze(intel_data=data)
    assert isinstance(result, AnalysisResult)
    assert result.status in ["success", "warning", "error"]


def test_validate(module):
    assert module.validate(None) is False
    assert module.validate({"k": "v"}) is True


def test_info(module):
    info = module.get_info()
    assert info["status"] == "Production"
