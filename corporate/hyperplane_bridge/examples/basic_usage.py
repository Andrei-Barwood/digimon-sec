import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from hyperplane_bridge.core import HyperplaneBridge


def main():
    module = HyperplaneBridge()
    data = {
    "connected_services": 14,
    "auth_failures_last_hour": 2,
    "schema_drift_detected": True,
    "rate_limit_events": 5,
}
    result = module.analyze(api_data=data)
    print(result.model_dump())


if __name__ == "__main__":
    main()
