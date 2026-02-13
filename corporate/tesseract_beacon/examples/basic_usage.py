import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from tesseract_beacon.core import TesseractBeacon


def main():
    module = TesseractBeacon()
    data = {
    "feed_count": 12,
    "ioc_overlap_ratio": 0.67,
    "stale_feed_detected": False,
    "high_confidence_iocs": 28,
}
    result = module.analyze(intel_data=data)
    print(result.model_dump())


if __name__ == "__main__":
    main()
