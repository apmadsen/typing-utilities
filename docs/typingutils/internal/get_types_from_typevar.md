[Documentation](/docs/documentation.md) > [typingutils](/docs/typingutils/module.md) > [internal](/docs/typingutils/internal/module.md)  > get_types_from_typevar

## get_types_from_typevar(typevar: _TypeVarParameter_) -> _TypeParameter | UnionParameter_

The `get_types_from_typevar` function returns the type constraints from the typevar or typevar tuple. If no constraints are specified, `type[Any]` is returned.

If typevar is a TypeVarTuple (new in Python 3.11), `tuple[type[Any], ...]` is returned..

### Example:
```python
T = TypeVar("T")
T1 = TypeVar("T1", bound = str)
Ts = TypeVarTuple("Ts")

get_types_from_typevar(T) # => type[Any]
get_types_from_typevar(T1) # => str
get_types_from_typevar(Ts) # => tuple[type[Any], ...]
```