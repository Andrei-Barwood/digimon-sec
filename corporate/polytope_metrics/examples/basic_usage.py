import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from polytope_metrics.core import PolytopeMetrics


def main():
    module = PolytopeMetrics()
    data = {
    "mttr_hours": 6,
    "mttd_hours": 3,
    "coverage_ratio": 0.79,
    "critical_alert_backlog": 14,
}
    result = module.analyze(metrics_data=data)
    print(result.model_dump())


if __name__ == "__main__":
    main()
