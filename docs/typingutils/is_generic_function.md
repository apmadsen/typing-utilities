[Documentation](/docs/documentation.md) > [typingutils](/docs/typingutils/module.md) > is_generic_function

## is_generic_function(fn: AnyFunction) -> _bool_

The `is_generic_function` function  indicates whether or not `fn` is a generic function. New in Python 3.12.

### Example:
```python
def function():
    ...

is_generic_function(function) # => False

def generic_function[T]():
    ...

is_generic_function(generic_function) # => True
```