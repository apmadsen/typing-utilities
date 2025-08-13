# pyright: basic
import sys

if sys.version_info >= (3, 11):

    from typing import Required # pyright: ignore[reportAssignmentType, reportAttributeAccessIssue]

else:

    from typing_extensions import Required # pyright: ignore[reportMissingModuleSource] # pragma: no cover
