[API](/docs/api.md) > typingutils module functions
# `typingutils` module functions

## issubclass_typing(cls: _AnyType_, base: _AnyType | TypeArgs_) -> _bool_

The `issubclass_typing` function extends the builtin `issubclass(cls, base)` function allowing both `cls` and `base` to be either a type, typevar or union object.

## is_optional(cls: _AnyType_) -> _bool_

The `is_optional` function checks whenter or not type is optional, i.e. a union containing `None` a `typing.Optional[T]` or `typing.Union[T, None]`

## is_union(cls: _AnyType_) -> _bool_

The `is_union` function checks whenter or not type is a union. This includes both `x|y` and `typing.Union` unions.

## is_subscripted_generic_type(cls: _AnyType_) -> _bool_

The `is_subscripted_generic_type` function indicates whether or not `cls` is a subscripted generic type as `list[str]` is a subscripted generic type of `list[T]` etc.

## is_generic_type(cls: _AnyType_) -> _bool_

The `is_generic_type` function  indicates whether or not `cls` is a generic type like `list[T]`.

## is_generic_function(fn: AnyFunction) -> _bool_

The `is_generic_function` function  indicates whether or not `fn` is a generic function. New in Python 3.12.

## get_type_name(cls: _AnyType_) -> _str_

The `get_type_name` function returns the name of type `cls`. It's used throughout the tests of this package and for documentational purposes.

## get_optional_type(cls: _AnyType_) -> _tuple[AnyType, bool]_

The `get_optional_type` function extracts any types from `cls` regardless if it's an ordinary type, a union or a `typing.Optional[T]` object, and returns it along with a bool indicatig if optional or not.

## isinstance_typing(obj: _Any_) -> _bool_

The `isinstance_typing` function checks whether or not `obj` is an instance of a class.

## isinstance_typing(obj: _Any_, cls: _AnyType | TypeArgs_, *, recursive: _bool_ = _False_) -> _bool_

The `isinstance_typing` function extends the builtin `isinstance(obj, cls)` function allowing `cls` to be either a type, typevar or union object. The `recursive` option allows for recursive or deep instance checking of collection types such as sequeces, mappings, sets and iterables.

## is_type(obj: Any) -> _bool_

The `is_type` function checks whenter or not `obj` is recognized as a type. This includes unions and `type[Any]`.

## check_type(obj: _Any_) -> _TypeCheck_

The `check_type` functions checks if `obj` is a type and in that case, also if it's a generic type or a subscripted generic type. It returns a `TypeCheck` NamedTuple instance.

### Example
```python
is_type, is_generic_type, subscripted_generic_type = check_type(cls)
```
## get_generic_arguments(obj: _Any_) -> _tuple[type|union, ...]_

The `get_generic_arguments` function returns the types used to create the subscripted generic type or instance `obj`.

## get_generic_parameters(obj: _TypeParameter | AnyFunction_) -> _tuple[type|union|TypeVar, ...]_

The `get_generic_parameters` function returns the typevars needed to create a subscripted generic type (or function if python>=3.12) derived from `obj`.
