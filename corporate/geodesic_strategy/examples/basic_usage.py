import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from geodesic_strategy.core import GeodesicStrategy


def main():
    module = GeodesicStrategy()
    data = {
    "risk_domains_pending": 4,
    "budget_alignment_score": 0.74,
    "control_gap_critical": 2,
    "board_priority_defined": True,
}
    result = module.analyze(strategy_data=data)
    print(result.model_dump())


if __name__ == "__main__":
    main()
