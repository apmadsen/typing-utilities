# pyright: basic
from typing import TypeVar, Iterable, Any, cast
from typingutils import get_type_name, TypeParameter, UnionParameter, AnyType


builtin_impl_failed: list[str] = []

def builtin(obj: Any, cls: TypeParameter | UnionParameter | tuple[TypeParameter | UnionParameter, ...] | TypeVar) -> bool | None:
    try:
        return isinstance(obj, cls) # pyright: ignore[reportArgumentType]
    except:
        builtin_impl_failed.append(f"isinstance({obj}, {get_type_name(cast(AnyType, cls))})")
        return None

implementations = [ builtin ]

try:

    from runtype import isa # pyright: ignore[reportMissingImports]
    runtype_impl_failed: list[str] = []

    def runtype(obj: Any, cls: TypeParameter | UnionParameter | tuple[TypeParameter | UnionParameter, ...] | TypeVar) -> bool | None:
        try:
            return isa(obj, cls) # pyright: ignore[reportArgumentType]
        except:
            runtype_impl_failed.append(f"isa({obj}, {get_type_name(cast(AnyType, cls))})")
            return None

    implementations.append(runtype)

except ImportError:
    pass

def comparison_generator(obj: Any, cls: TypeParameter | UnionParameter | tuple[TypeParameter | UnionParameter, ...] | TypeVar) -> Iterable[tuple[str, bool | None]]:
    for impl in implementations:
        yield getattr(impl, "__name__"), impl(obj, cls)