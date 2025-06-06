[API](/docs/api.md) > [typingutils](/docs/api/typingutils/typingutils.md) > get_optional_type

## get_optional_type(cls: _AnyType_) -> _tuple[AnyType, bool]_

The `get_optional_type` function extracts any types from `cls` regardless if it's an ordinary type, a union or a `typing.Optional[T]` object, and returns it along with a bool indicatig if optional or not.

### Example:
```python
get_optional_type(str | int) # => (str|int, False)
get_optional_type(str | int |None) # => (str|int, True)
```