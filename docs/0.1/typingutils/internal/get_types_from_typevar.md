[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [typingutils](/docs/0.1/typingutils/module.md) >
   [internal](/docs/0.1/typingutils/internal/module.md) >
    get_types_from_typevar

# get_types_from_typevar(typevar: _[TypeVarParameter](../typevar_parameter.md)_) -> _[TypeParameter](../type_parameter.md) | [UnionParameter](../union_parameter.md)_

The `get_types_from_typevar` function returns the type constraints from the typevar or typevar tuple. If no constraints are specified, `type[Any]` is returned.

If typevar is a TypeVarTuple (new in Python 3.11), `tuple[type[Any], ...]` is returned.

## Parameters

- typevar `TypeVarParameter`: A typevar or typevar tuple.

### Example:
```python
T = TypeVar("T")
T1 = TypeVar("T1", bound = str)
Ts = TypeVarTuple("Ts")

get_types_from_typevar(T) # => type[Any]
get_types_from_typevar(T1) # => str
get_types_from_typevar(Ts) # => tuple[type[Any], ...]
```