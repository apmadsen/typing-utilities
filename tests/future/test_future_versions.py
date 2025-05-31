# pyright: basic
import sys

if sys.version_info >= (3, 11):
    from tests.future.py311 import TestPython311

if sys.version_info >= (3, 12):
    from tests.future.py312 import TestPython312
