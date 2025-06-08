[Documentation](/docs/documentation.md) >
 [v0.0](/docs/0.0/version.md) >
  [typingutils](/docs/0.0/typingutils/module.md) >
   get_generic_parameters

## get_generic_parameters(obj: _TypeParameter | AnyFunction_) -> _tuple[type|union|TypeVar, ...]_

The `get_generic_parameters` function returns the typevars needed to create a subscripted generic type (or function if python>=3.12) derived from `obj`.

### Example:
```python
class GenericClass[T]:
    ...

get_generic_parameters(GenericClass) # => (T,)

def generic_function[T]():
    ...

get_generic_parameters(generic_function) # => (T,)
```