import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from torus_audit.core import TorusAudit


def main():
    module = TorusAudit()
    data = {
    "unsigned_events_detected": 2,
    "log_retention_gap_days": 5,
    "tamper_suspected": True,
    "critical_event_loss": False,
}
    result = module.analyze(audit_data=data)
    print(result.model_dump())


if __name__ == "__main__":
    main()
