[Documentation](/docs/documentation.md) > [typingutils](/docs/typingutils/module.md) > is_optional

## is_optional(cls: _AnyType_) -> _bool_

The `is_optional` function checks whenter or not type is optional, i.e. a union containing `None` a `typing.Optional[T]` or `typing.Union[T, None]`

### Example:
```python
is_optional(str | int) # => False
is_optional(str | int |None) # => True
```