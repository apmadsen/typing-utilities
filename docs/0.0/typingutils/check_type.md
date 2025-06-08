[Documentation](/docs/documentation.md) >
 [v0.0](/docs/0.0/version.md) >
  [typingutils](/docs/0.0/typingutils/module.md) >
   check_type

## check_type(obj: _Any_) -> _TypeCheck_

The `check_type` functions checks if `obj` is a type and in that case, also if it's a generic type or a subscripted generic type. It returns a `TypeCheck` NamedTuple instance.

### Example
```python
is_type, is_generic_type, subscripted_generic_type = check_type(cls)
```