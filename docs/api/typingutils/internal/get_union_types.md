[API](/docs/api.md) > [typingutils](/docs/api/typingutils/typingutils.md) > [internal](/docs/api/typingutils/internal/internal.md)  > get_union_types

## get_union_types(cls: _UnionParameter_) -> _TypeParameter_

The `get_union_types` function returns the types which make up the specified union.

### Example:
```python
get_union_types(int | None) # => (int,)
get_union_types(int | str | None) # => (int, str)
```