[Documentation](/docs/documentation.md) >
 [v0.0](/docs/0.0/version.md) >
  [typingutils](/docs/0.0/typingutils/module.md) >
   is_optional

## is_optional(cls: _AnyType_) -> _bool_

The `is_optional` function checks whenter or not type is optional, i.e. a union containing `None` a `typing.Optional[T]` or `typing.Union[T, None]`

### Example:
```python
is_optional(str | int) # => False
is_optional(str | int |None) # => True
```