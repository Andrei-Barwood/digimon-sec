import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from manifold_conductor.core import ManifoldConductor


def main():
    module = ManifoldConductor()
    data = {
    "playbooks_available": 18,
    "automation_success_rate": 0.86,
    "manual_steps_remaining": 7,
    "critical_workflow_timeout": False,
}
    result = module.analyze(orchestration_data=data)
    print(result.model_dump())


if __name__ == "__main__":
    main()
