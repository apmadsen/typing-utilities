[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [typingutils](/docs/0.1/typingutils/module.md) >
   is_optional

# is_optional(cls: _[AnyType](any_type.md)_) -> _bool_

The `is_optional` function checks whenter or not type is optional, i.e. a union containing `None` a `typing.Optional[T]` or `typing.Union[T, None]`

## Parameters

- cls `AnyType`: A type.

### Example:
```python
is_optional(str | int) # => False
is_optional(str | int |None) # => True
```