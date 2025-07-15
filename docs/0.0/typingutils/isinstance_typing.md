[Documentation](/docs/documentation.md) >
 [v0.0](/docs/0.0/version.md) >
  [typingutils](/docs/0.0/typingutils/module.md) >
   isinstance_typing

# isinstance_typing(obj: _Any_) -> _bool_

The `isinstance_typing` function checks whether or not `obj` is an instance of a class.

## Parameters

- obj `Any`: A type, object or instance of an object.

### Example:
```python
isinstance_typing(list) # => False
isinstance_typing([1,2,3]) # => True
```

## isinstance_typing(obj: _Any_, cls: _[AnyType](any_type.md) | [TypeArgs](type_args.md)_, *, recursive: _bool_ = _False_) -> _bool_

The `isinstance_typing` function extends the builtin `isinstance(obj, cls)` function allowing `cls` to be either a type, typevar or union object. The `recursive` option allows for recursive or deep instance checking of collection types such as sequeces, mappings, sets and iterables.

## Parameters

- obj `Any`: A type, object or instance of an object.
- cls `AnyType | TypeArgs`: A type to compare with.

### Example:
```python
isinstance_typing("abc", str) # => True
isinstance_typing("abc", type[Any]) # => True
isinstance_typing("abc", abc.Collection) # => True
isinstance_typing([1,2,3], list) # => True
isinstance_typing([1,2,3], typing.List) # => True
isinstance_typing([1,2,3], abc.Collection) # => True
isinstance_typing([1,2,3], abc.Sequence) # => True
isinstance_typing([1,2,3], abc.MutableSequence) # => True
isinstance_typing([1,2,3], list[Any]) # => True
isinstance_typing([1,2,3], list[int], recursive = True) # => True
isinstance_typing({"a": 1, "b": 2}, dict[str, int], recursive = True) # => True
```