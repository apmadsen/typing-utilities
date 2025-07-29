[Documentation](/docs/documentation.md) >
 [v0.0](/docs/0.0/version.md) >
  [typingutils](/docs/0.0/typingutils/module.md) >
   is_variadic_tuple_type

# is_variadic_tuple_type(cls: _type[tuple[Any, ...]]_) -> _bool_

The `is_variadic_tuple_type` function  indicates whether or not `cls` is a variadic tuple type, eg. `tuple[str, ...]`.

## Parameters

- cls `type[tuple[Any, ...]]`: A type.

### Example:
```python
is_variadic_tuple_type(tuple[str, ...]) # => True
is_variadic_tuple_type(tuple[str, int]) # => False
```