[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [typingutils](/docs/0.1/typingutils/module.md) >
   is_annotated_type

# is_annotated_type(obj: _Any_) -> _bool_

The `is_annotated_type` function checks whenter or not object is an annotated type.

Supported annotations are Annotated, Required, NotRequired, ReadOnly, ClassVar and Final.

## Parameters

- obj `Any`: The object to check.

### Example:
```python
is_annotated_type(Annotated[int|str, "an integer or a string"]) # => True
```