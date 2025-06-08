[Documentation](/docs/documentation.md) >
 [v0.0](/docs/0.0/version.md) >
  [typingutils](/docs/0.0/typingutils/module.md) >
   is_generic_type

## is_generic_type(cls: _AnyType_) -> _bool_

The `is_generic_type` function  indicates whether or not `cls` is a generic type like `list[T]`.

### Example:
```python
class GenericClass[T]:
    ...

is_generic_type(GenericClass[T]) # => True

gc = GenericClass[T]()
is_generic_type(gc) # => False
```