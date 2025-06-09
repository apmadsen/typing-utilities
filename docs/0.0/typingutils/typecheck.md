[Documentation](/docs/documentation.md) >
 [v0.0](/docs/0.0/version.md) >
  [typingutils](/docs/0.0/typingutils/module.md) >
   TypeCheck

# TypeCheck class : NamedTuple

The `TypeCheck` class is a NamedTuple subclass containing the fields `is_type: bool`, `is_generic_type: bool` and `is_subscripted_generic_type: bool` and is returned by the function `check_type()`. The three fields  corresponds to value returned by the functions of the same names.


### Example
```python
type_check = check_type(cls) # is equivalent to
is_type, is_generic_type, subscripted_generic_type = check_type(cls)
```