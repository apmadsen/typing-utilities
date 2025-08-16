[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [typingutils](/docs/0.1/typingutils/module.md) >
   get_generic_parameters

# get_generic_parameters(obj: _[TypeParameter](type_parameter.md) | [AnyFunction](any_function.md)_) -> _tuple[TypeVar, ...]_

The `get_generic_parameters` function returns the typevars needed to create a subscripted generic type (or function if python>=3.12) derived from `obj`.

## Parameters

- obj `TypeParameter | AnyFunction`: A type or function.

# get_generic_parameters(obj: _[TypeParameter](type_parameter.md) | [AnyFunction](any_function.md)_, *, extract_types_from_typevars: bool = False) -> _[TypeArgs](type_args.md)_

The `get_generic_parameters` function returns the typevars needed to create a subscripted generic type (or function if python>=3.12) derived from `obj`.

## Parameters

- obj `TypeParameter | AnyFunction`: A type or function.
- extract_types_from_typevars `bool`: Tries to extract types from TypeVars (if bound).

### Example:
```python
class GenericClass[T]:
    ...

get_generic_parameters(GenericClass) # => (T,)

def generic_function[T]():
    ...

get_generic_parameters(generic_function) # => (T,)
```