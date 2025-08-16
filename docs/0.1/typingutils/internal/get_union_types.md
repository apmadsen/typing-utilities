[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [typingutils](/docs/0.1/typingutils/module.md) >
   [internal](/docs/0.1/typingutils/internal/module.md) >
    get_union_types

# get_union_types(cls: _[UnionParameter](../union_parameter.md)_) -> [TypeParameter](../type_parameter.md)_

The `get_union_types` function returns the types which make up the specified union.

## Parameters

- cls `UnionParameter`: A union of types.

### Example:
```python
get_union_types(int | None) # => (int,)
get_union_types(int | str | None) # => (int, str)
```