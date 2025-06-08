[Documentation](/docs/documentation.md) >
 [v0.0](/docs/0.0/version.md) >
  [typingutils](/docs/0.0/typingutils/module.md) >
   is_subscripted_generic_type

## is_subscripted_generic_type(cls: _AnyType_) -> _bool_

The `is_subscripted_generic_type` function indicates whether or not `cls` is a subscripted generic type as `list[str]` is a subscripted generic type of `list[T]` etc.

### Example:
```python
class GenericClass[T]:
    ...

is_subscripted_generic_type(GenericClass[T]) # => False

gc = GenericClass[T]()
is_subscripted_generic_type(gc) # => True
```