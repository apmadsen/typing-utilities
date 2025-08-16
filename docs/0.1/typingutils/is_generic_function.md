[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [typingutils](/docs/0.1/typingutils/module.md) >
   is_generic_function

# is_generic_function(fn: _[AnyFunction](any_function.md)_) -> _bool_

The `is_generic_function` function  indicates whether or not `fn` is a generic function. New in Python 3.12.

## Parameters

- fn `AnyFunction`: A function.

### Example:
```python
def function():
    ...

is_generic_function(function) # => False

def generic_function[T]():
    ...

is_generic_function(generic_function) # => True
```