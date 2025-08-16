# pyright: basic
# ruff: noqa
from typing import TypeVar, Iterable, cast
from typingutils import get_type_name, TypeParameter, UnionParameter, AnyType
from os import getenv

from tests.other_impl.impl_error import ImplError

builtin_impl_failed: list[str] = []

IMPL_ERROR = ImplError()

def builtin(cls: TypeParameter | UnionParameter, base: TypeParameter | UnionParameter | TypeVar | tuple[TypeParameter | UnionParameter | TypeVar, ...]) -> bool | ImplError:
    try:
        return issubclass(cls, base) # pyright: ignore[reportArgumentType]
    except:
        builtin_impl_failed.append(f"issubclass({get_type_name(cls)}, {get_type_name(cast(AnyType, base))})")
        return IMPL_ERROR

implementations = [ builtin ]

try:

    from typing_utils import issubtype # pyright: ignore[reportUnknownVariableType,reportMissingImports]
    typing_utils_impl_failed: list[str] = []

    def typing_utils(cls: TypeParameter | UnionParameter, base: TypeParameter | UnionParameter | TypeVar | tuple[TypeParameter | UnionParameter | TypeVar, ...]) -> bool | ImplError:
        try:
            result = issubtype(cls, base) # pyright: ignore[reportArgumentType]
            return IMPL_ERROR if result is None else result
        except:
            typing_utils_impl_failed.append(f"issubclass({get_type_name(cls)}, {get_type_name(cast(AnyType, base))})")
            return IMPL_ERROR

    implementations.append(typing_utils)

except ImportError:
    pass

try:

    from runtype import issubclass # pyright: ignore[reportMissingImports]
    runtype_impl_failed: list[str] = []

    def runtype(cls: TypeParameter | UnionParameter, base: TypeParameter | UnionParameter | TypeVar | tuple[TypeParameter | UnionParameter | TypeVar, ...]) -> bool | ImplError:
        try:
            return issubclass(cls, base) # pyright: ignore[reportArgumentType]
        except:
            runtype_impl_failed.append(f"issubclass({get_type_name(cls)}, {get_type_name(cast(AnyType, base))})")
            return IMPL_ERROR

    implementations.append(runtype)

except ImportError:
    pass

def comparison_generator(cls: TypeParameter | UnionParameter, base: TypeParameter | UnionParameter | TypeVar | tuple[TypeParameter | UnionParameter | TypeVar, ...]) -> Iterable[tuple[str, bool | ImplError]]:
    if getenv("TESTS_EXTENSIVE_DEBUGGING", "").lower() in ("1", "true"):
        for impl in implementations:
            yield getattr(impl, "__name__"), impl(cls, base)