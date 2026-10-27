# pyright: basic
# ruff: noqa
import sys

if sys.version_info >= (3, 12):
    from tests.future.py312 import TestPython312
