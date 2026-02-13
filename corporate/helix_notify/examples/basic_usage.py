import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from helix_notify.core import HelixNotify


def main():
    module = HelixNotify()
    data = {
    "critical_alerts_pending": 3,
    "escalation_delay_minutes": 22,
    "channel_delivery_failures": 1,
    "oncall_ack_missing": True,
}
    result = module.analyze(notification_data=data)
    print(result.model_dump())


if __name__ == "__main__":
    main()
