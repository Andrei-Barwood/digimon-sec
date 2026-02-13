import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from polyhedron_core.core import PolyhedronCore


def main():
    module = PolyhedronCore()
    data = {
    "module_health_degraded": 2,
    "pipeline_dependency_breaks": 1,
    "critical_contract_violation": True,
    "core_sync_delay_ms": 640,
}
    result = module.analyze(framework_data=data)
    print(result.model_dump())


if __name__ == "__main__":
    main()
