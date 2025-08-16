[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [typingutils](/docs/0.1/typingutils/module.md) >
   check_type

# check_type(obj: _Any_) -> _[TypeCheck](typecheck.md)_

The `check_type` functions checks if `obj` is a type and in that case, also if it's a generic type or a subscripted generic type. It returns a `TypeCheck` NamedTuple instance.

## Parameters

- obj `Any`: A type or an instance of an object.

### Example
```python
is_type, is_generic_type, subscripted_generic_type = check_type(cls)
```