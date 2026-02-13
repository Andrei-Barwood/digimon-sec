import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from simplex_ticket.core import SimplexTicket


def main():
    module = SimplexTicket()
    data = {
    "untriaged_alerts": 19,
    "sla_risk_tickets": 5,
    "duplicate_ticket_ratio": 0.18,
    "critical_owner_missing": True,
}
    result = module.analyze(ticket_data=data)
    print(result.model_dump())


if __name__ == "__main__":
    main()
