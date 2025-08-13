# pyright: basic
import sys

if sys.version_info >= (3, 11):

    from typing import LiteralString # pyright: ignore[reportAssignmentType, reportAttributeAccessIssue]

else:

    from typing_extensions import LiteralString # pyright: ignore[reportMissingModuleSource] # pragma: no cover
