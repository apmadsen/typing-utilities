# pyright: basic
from typing import TypeVar, Iterable, cast
from typingutils import get_type_name, TypeParameter, UnionParameter, AnyType


builtin_impl_failed: list[str] = []


def builtin(cls: TypeParameter | UnionParameter, base: TypeParameter | UnionParameter | TypeVar | tuple[TypeParameter | UnionParameter | TypeVar, ...]) -> bool | None:
    try:
        return issubclass(cls, base) # pyright: ignore[reportArgumentType]
    except:
        builtin_impl_failed.append(f"issubclass({get_type_name(cls)}, {get_type_name(cast(AnyType, base))})")
        return None

implementations = [ builtin ]

try:

    from typing_utils import issubtype # pyright: ignore[reportUnknownVariableType,reportMissingImports]
    typing_utils_impl_failed: list[str] = []

    def typing_utils(cls: TypeParameter | UnionParameter, base: TypeParameter | UnionParameter | TypeVar | tuple[TypeParameter | UnionParameter | TypeVar, ...]) -> bool | None:
        try:
            return issubtype(cls, base) # pyright: ignore[reportArgumentType]
        except:
            typing_utils_impl_failed.append(f"issubclass({get_type_name(cls)}, {get_type_name(cast(AnyType, base))})")
            return None

    implementations.append(typing_utils)

except ImportError:
    pass

try:

    from runtype import issubclass # pyright: ignore[reportMissingImports]
    runtype_impl_failed: list[str] = []

    def runtype(cls: TypeParameter | UnionParameter, base: TypeParameter | UnionParameter | TypeVar | tuple[TypeParameter | UnionParameter | TypeVar, ...]) -> bool | None:
        try:
            return issubclass(cls, base) # pyright: ignore[reportArgumentType]
        except:
            runtype_impl_failed.append(f"issubclass({get_type_name(cls)}, {get_type_name(cast(AnyType, base))})")
            return None

    implementations.append(runtype)

except ImportError:
    pass

def comparison_generator(cls: TypeParameter | UnionParameter, base: TypeParameter | UnionParameter | TypeVar | tuple[TypeParameter | UnionParameter | TypeVar, ...]) -> Iterable[tuple[str, bool | None]]:
    for impl in implementations:
        yield getattr(impl, "__name__"), impl(cls, base)