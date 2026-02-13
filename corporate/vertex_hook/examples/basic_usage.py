import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from vertex_hook.core import VertexHook


def main():
    module = VertexHook()
    data = {
    "unsigned_payload_attempts": 3,
    "delivery_failures": 4,
    "retry_queue_depth": 11,
    "critical_endpoint_latency_ms": 920,
}
    result = module.analyze(webhook_data=data)
    print(result.model_dump())


if __name__ == "__main__":
    main()
