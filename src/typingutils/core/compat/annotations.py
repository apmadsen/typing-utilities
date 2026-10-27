# pyright: basic
# ruff: noqa
import sys

if sys.version_info >= (3, 13):

    from typing import ReadOnly # pyright: ignore[reportAssignmentType, reportAttributeAccessIssue]

else:

    from typing_extensions import ReadOnly # pyright: ignore[reportMissingModuleSource] # pragma: no cover
