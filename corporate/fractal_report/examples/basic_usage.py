import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from fractal_report.core import FractalReport


def main():
    module = FractalReport()
    data = {
    "critical_findings": 6,
    "sla_breaches": 2,
    "executive_summary_ready": True,
    "evidence_coverage_ratio": 0.91,
}
    result = module.analyze(report_data=data)
    print(result.model_dump())


if __name__ == "__main__":
    main()
