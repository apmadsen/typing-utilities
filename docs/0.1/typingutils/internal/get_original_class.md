[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [typingutils](/docs/0.1/typingutils/module.md) >
   [internal](/docs/0.1/typingutils/internal/module.md) >
    get_original_class

# get_original_class(cls: _[AnyType](../any_type.md)_) -> _[TypeParameter](../type_parameter.md)_

The `get_original_class` function returns the original generic type from a class instance. This is useful for generic types because instances of these doesn't derive from them, thus having no generic arguments specified. Will even work when called from within a constructor of a class. Note that it doesn't work with builtin generic types like list[T].

## Parameters

- obj `Any`: An instance of a class.

### Example:
```python
class GenericClass[T]:
    def __init__(self):
        self.cls = get_original_class(self)
        self.args = get_generic_arguments(self)

gc = GenericClass[str]()
get_original_class(gc) # => GenericClass[str]
gc.cls # => GenericClass[str]
```