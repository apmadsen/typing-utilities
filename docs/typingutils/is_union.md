[Documentation](/docs/documentation.md) > [typingutils](/docs/typingutils/module.md) > is_union

## is_union(cls: _AnyType_) -> _bool_

The `is_union` function checks whenter or not type is a union. This includes both `x|y` and `typing.Union` unions.

### Example:
```python
is_union(str) # => False
is_union(str | int) # => True
```