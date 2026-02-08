"""
Pytest configuration for lemniscate_mnemo tests.

Ensures the src/ directory is on sys.path so imports work without an
editable install.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))





