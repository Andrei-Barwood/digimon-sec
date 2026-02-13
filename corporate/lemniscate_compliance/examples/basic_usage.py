import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from lemniscate_compliance.core import LemniscateCompliance


def main():
    module = LemniscateCompliance()
    data = {
    "failed_controls": 4,
    "evidence_missing_items": 9,
    "policy_drift_detected": True,
    "audit_window_days": 21,
}
    result = module.analyze(compliance_data=data)
    print(result.model_dump())


if __name__ == "__main__":
    main()
