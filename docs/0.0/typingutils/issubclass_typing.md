[Documentation](/docs/documentation.md) >
 [v0.0](/docs/0.0/version.md) >
  [typingutils](/docs/0.0/typingutils/module.md) >
   issubclass_typing

# issubclass_typing(cls: _[AnyType](any_type.md)_, base: _[AnyType](any_type.md) | [TypeArgs](type_args.md)_) -> _bool_

The `issubclass_typing` function extends the builtin `issubclass(cls, base)` function allowing both `cls` and `base` to be either a type, typevar or union object.

## Parameters

- cls `AnyType`: A type.
- base `AnyType | TypeArgs`: A type or TypeVar to compare with.

###

### Example:
```python
issubclass_typing(tuple, object) # => True
issubclass_typing(tuple, tuple) # => True
issubclass_typing(tuple, type[Any]) # => True
issubclass_typing(tuple[str], tuple) # => True
issubclass_typing(tuple[str], tuple[Any]) # => True

issubclass_typing(str, (str, int, bool)) # => True
issubclass_typing(str, (int, bool)) # => False

issubclass_typing(str, int | bool) # => False
issubclass_typing(str, str | float) # => True

issubclass_typing(str, TypeVar("T")) # => True
issubclass_typing(str, TypeVar("T", bound = str)) # => True
issubclass_typing(str, TypeVar("T", bound = int)) # => False
```