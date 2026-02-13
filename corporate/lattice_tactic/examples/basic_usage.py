import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from lattice_tactic.core import LatticeTactic


def main():
    module = LatticeTactic()
    data = {
    "campaign_links_found": 5,
    "ttp_matches": 9,
    "sector_relevance_score": 0.82,
    "active_adversary_signal": True,
}
    result = module.analyze(cti_data=data)
    print(result.model_dump())


if __name__ == "__main__":
    main()
