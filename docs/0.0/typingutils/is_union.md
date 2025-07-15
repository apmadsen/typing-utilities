[Documentation](/docs/documentation.md) >
 [v0.0](/docs/0.0/version.md) >
  [typingutils](/docs/0.0/typingutils/module.md) >
   is_union

# is_union(cls: _[AnyType](any_type.md)_) -> _bool_

The `is_union` function checks whenter or not type is a union. This includes both `x|y` and `typing.Union` unions.

## Parameters

- cls `AnyType`: A type.

### Example:
```python
is_union(str) # => False
is_union(str | int) # => True
```