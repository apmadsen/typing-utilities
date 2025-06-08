[Documentation](/docs/documentation.md) >
 [v0.0](/docs/0.0/version.md) >
  [typingutils](/docs/0.0/typingutils/module.md) >
   [internal](/docs/0.0/typingutils/internal/module.md) >
    get_executing_function

## get_executing_function() -> _AnyFunction | None_

The `get_executing_function` function returns the executing function from within, enabling retrieval of its generic parameters via the `get_generic_parameters` function.

### Example:
```python
def function(arg1: int, arg2: int) -> tuple[AnyFunction, TypeArgs] | None:
    if fn := get_executing_function():
        args = get_generic_parameters(fn)
        return fn, args

function(1,2) # => Function function, ()

def generic_function[T](arg1: T, arg2: int) -> tuple[AnyFunction, TypeArgs] | None:
    if fn := get_executing_function():
        args = get_generic_parameters(fn)
        return fn, args

generic_function(1,2) # => Function function, (T)
```