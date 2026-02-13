"""
Unit tests for SimplexTicket (Production)
"""

import pytest

from simplex_ticket.core import SimplexTicket
from simplex_ticket.models import AnalysisResult, DetectionReport


@pytest.fixture
def module():
    return SimplexTicket()


def test_init_default(module):
    assert module.name == "Simplex Ticket"
    assert module.mission == "Fleeting Joy"
    assert module.role == "ticketing-engine"


def test_primary_method(module):
    data = {
    "untriaged_alerts": 19,
    "sla_risk_tickets": 5,
    "duplicate_ticket_ratio": 0.18,
    "critical_owner_missing": True,
}
    report = module.create_security_tickets(data)
    assert isinstance(report, DetectionReport)
    assert report.total_checks > 0


def test_analyze(module):
    data = {
    "untriaged_alerts": 19,
    "sla_risk_tickets": 5,
    "duplicate_ticket_ratio": 0.18,
    "critical_owner_missing": True,
}
    result = module.analyze(ticket_data=data)
    assert isinstance(result, AnalysisResult)
    assert result.status in ["success", "warning", "error"]


def test_validate(module):
    assert module.validate(None) is False
    assert module.validate({"k": "v"}) is True


def test_info(module):
    info = module.get_info()
    assert info["status"] == "Production"
