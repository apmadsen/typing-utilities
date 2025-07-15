[Documentation](/docs/documentation.md) >
 [v0.0](/docs/0.0/version.md) >
  [typingutils](/docs/0.0/typingutils/module.md) >
   get_generic_arguments

# get_generic_arguments(obj: _Any_) -> _tuple[type|union, ...]_

The `get_generic_arguments` function returns the types used to create the subscripted generic type or instance `obj` even from within a constructor.

## Parameters

- obj `Any`: An instance of an object.

### Example:
```python
class GenericClass[T]:
    def __init__(self):
        self.args = get_generic_arguments(self)

gc = GenericClass[str]()
get_generic_arguments(gc) # => (str,)
gc.args # => (str,)
```