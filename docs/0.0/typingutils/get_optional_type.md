[Documentation](/docs/documentation.md) >
 [v0.0](/docs/0.0/version.md) >
  [typingutils](/docs/0.0/typingutils/module.md) >
   get_optional_type

# get_optional_type(cls: _[AnyType](any_type.md)_) -> _tuple[[AnyType](any_type.md), bool]_

The `get_optional_type` function extracts any types from `cls` regardless if it's an ordinary type, a union or a `typing.Optional[T]` object, and returns it along with a bool indicatig if optional or not.

## Parameters

- cls `AnyType`: A type.

### Example:
```python
get_optional_type(str | int) # => (str|int, False)
get_optional_type(str | int |None) # => (str|int, True)
```