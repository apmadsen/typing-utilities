# pyright: basic
import sys

if sys.version_info >= (3, 11):

    from typing import NotRequired # pyright: ignore[reportAssignmentType, reportAttributeAccessIssue]

else:

    from typing_extensions import NotRequired # pyright: ignore[reportMissingModuleSource] # pragma: no cover
