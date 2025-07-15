[Documentation](/docs/documentation.md) >
 [v0.0](/docs/0.0/version.md) >
  [typingutils](/docs/0.0/typingutils/module.md) >
   [internal](/docs/0.0/typingutils/internal/module.md) >
    get_generic_origin

# get_generic_origin(cls: _[AnyType](../any_type.md)_) -> _[TypeParameter](../type_parameter.md)_

The `get_generic_origin` function returns the generic origin of a type i.e. the type a generic type originates from.

## Parameters

- cls `AnyType`: A type.

### Example:
```python
get_generic_origin(tuple[T]) # => tuple
get_generic_origin(tuple[int]) # => tuple
```