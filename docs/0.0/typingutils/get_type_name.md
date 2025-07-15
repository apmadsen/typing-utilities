[Documentation](/docs/documentation.md) >
 [v0.0](/docs/0.0/version.md) >
  [typingutils](/docs/0.0/typingutils/module.md) >
   get_type_name

# get_type_name(cls: _[AnyType](any_type.md)_) -> _str_

The `get_type_name` function returns the name of type `cls`. It's used throughout the tests of this package and for documentational purposes.

## Parameters

- cls `AnyType`: A type.

### Example:
```python
get_type_name(TypeVarTyple("Ts")) # => "*Ts"
get_type_name(TypeVar("T")) # => "T"
get_type_name(TypeVar("T", bound = str)) # => "T<str>"
get_type_name(TypeVar("T", (str, int))) # => "T<str|int>"
get_type_name(types.EllipsisType) # => "..."
get_type_name(types.NoneType) # => "None"
get_type_name(list[str]) # => "list[str]"
get_type_name(dict[str, Any]) # => "dict[str, Any]"
get_type_name(str | int) # => "str | int"
get_type_name((str, int)) # => "(str, int)"
```