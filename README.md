[![Test](https://github.com/apmadsen/typing-utilities/actions/workflows/python-test.yml/badge.svg)](https://github.com/apmadsen/typing-utilities/actions/workflows/python-test.yml)
[![Coverage](https://github.com/apmadsen/typing-utilities/actions/workflows/python-test-coverage.yml/badge.svg)](https://github.com/apmadsen/typing-utilities/actions/workflows/python-test-coverage.yml)
[![Stable Version](https://img.shields.io/pypi/v/typing-utilities?label=stable&sort=semver&color=blue)](https://github.com/apmadsen/typing-utilities/releases)
![Pre-release Version](https://img.shields.io/github/v/release/apmadsen/typing-utilities?label=pre-release&include_prereleases&sort=semver&color=blue)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/typing-utilities)
[![PyPI Downloads](https://static.pepy.tech/badge/typing-utilities/week)](https://pepy.tech/projects/typing-utilities)

# typing-utilities: Runtime reflection and validation of types and generics.

typing-utilities extends Python with the ability to check instances and types of generic types and unions introduced in the `typing` module.

Following is a small example of two of the most usable functions `issubclass_typing` and `isinstance_typing`, but a lot more is to be found in the API section further down...

## Example:

```python
from typing import Generic, TypeVar
from typingutils import issubclass_typing, isinstance_typing

T = TypeVar('T')

class Class1(Generic[T]):
    pass

class_type1 = Class1[str]
class_type2 = Class1[int]

issubclass_typing(class_type1, class_type2) # => False

# next line will fail
issubclass(class_type1, class_type2) # => TypeErrorr: Subscripted generics cannot be used with class and instance checks

class_inst1 = class_type1()
class_inst2 = class_type2()

isinstance_typing(class_inst1, class_type1) # => True
isinstance_typing(class_inst1, class_type2) # => False
isinstance_typing(class_inst2, class_type2) # => True
isinstance_typing(class_inst2, class_type1) # => False

# next line will fail
isinstance(class_inst1, class_type1) # => TypeError: Subscripted generics cannot be used with class and instance checks
```

## Conventions

This project differs from Python and other projects in some aspects:

- Generic subscripted types like `list[str]` are always a subclass of its base type `list` whereas the opposite is not true.
- Any type is a subclass of `type[Any]`.
- `type[Any]` is not an instance of `type[Any]`.
- Builtin types and `typing` types are interchangeable, i.e. `list[T]` is interchangeable with `typing.List[T]` etc.

## What's not included

### Deep validation checks

This project does not check the contents of objects like lists and dicts, which is why `isinstance_typing([1, 2, 3], list[int])` returns false. The reason is, that while it's relatively easy to compare every item in a list to the type argument of `list[str]`, other generic types are not as straight forward, thus it's better left to the programmer.

### Generic types

It's not the goal of this project to deliver generic types such as generically enforced lists and dicts.

## API

All functions and classes are available in the `typingutils` and `typingutils.internal` modules.

### Variables

#### TypeParameter

The `TypeParameter` variable is an annotation of `type | type[Any]` and matches any ordinary type.

#### UnionParameter

The `UnionParameter` variable is an annotation of `UnionType | tuple[TypeParameter, ...]` and matches any type union.

#### AnyType

The `AnyType` variable is an annotation of `TypeParameter | UnionParameter | TypeVar]` and matches any type, typevar or union.

#### TypeArgs

The `TypeArgs` variable is an annotation of `tuple[AnyType, ...]` and matches any sequence of types, typevars or unions.

### Functions

#### issubclass_typing(cls: _AnyType_, base: _AnyType | TypeArgs_) -> _bool_

The `issubclass_typing` function extends the builtin `issubclass(cls, base)` function allowing both `cls` and `base` to be either a type, typevar or union object.

#### is_optional(cls: _AnyType_) -> _bool_

The `is_optional` function checks whenter or not type is optional, i.e. a union containing `None` a `typing.Optional[T]` or `typing.Union[T, None]`

#### is_union(cls: _AnyType_) -> _bool_

The `is_union` function checks whenter or not type is a union. This includes both `x|y` and `typing.Union` unions.

#### is_subscripted_generic_type(cls: _AnyType_) -> _bool_

The `is_subscripted_generic_type` function indicates whether or not `cls` is a subscripted generic type as `list[str]` is a subscripted generic type of `list[T]` etc.

#### is_generic_type(cls: _AnyType_) -> _bool_

The `is_generic_type` function  indicates whether or not `cls` is a generic type like `list[T]`.

#### get_type_name(cls: _AnyType_) -> _str_

The `get_type_name` function returns the name of type `cls`. It's used throughout the tests of this package and for documentational purposes.

#### get_optional_type(cls: _AnyType_) -> _tuple[AnyType, bool]_

The `get_optional_type` function extracts any types from `cls` regardless if it's an ordinary type, a union or a `typing.Optional[T]` object, and returns it along with a bool indicatig if optional or not.

#### isinstance_typing(obj: _Any_) -> _bool_

The `isinstance_typing` function checks whether or not `obj` is an instance of a class.

#### isinstance_typing(obj: _Any_, cls: _AnyType | TypeArgs_) -> _bool_

The `isinstance_typing` function extends the builtin `isinstance(obj, cls)` function allowing `cls` to be either a type, typevar or union object.

#### is_type(obj: Any) -> _bool_

The `is_type` function checks whenter or not `obj` is recognized as a type. This includes unions and `type[Any]`.

#### get_generic_arguments(obj: _Any_) -> _tuple[type|union, ...]_

The `get_generic_arguments` function returns the types used to create the subscripted generic type or instance `obj`.

#### get_generic_parameters(cls: _AnyType_) -> _tuple[type|union|TypeVar, ...]_

The `get_generic_parameters` function returns the typevars needed to create a subscripted generic type derived frol `cls`.

#### internal.get_generic_origin(cls: _AnyType_) -> _TypeParameter_

The `get_generic_origin` function returns the generic origin of a type i.e. the type a generic type originates from.

#### internal.get_union_types(cls: _UnionParameter_) -> _TypeParameter_

The `get_union_types` function returns the types which make up the specified union.

#### internal.get_original_class(cls: AnyType) -> _TypeParameter_

The `get_original_class` function returns the original generic type from a class instance. This is useful for generic types because instances of these doesn't derive from them, thus having no generic arguments specified. Will even work when called from within a constructor of a class. Note that it doesn't work with builtin generic types like list[T].

#### internal.get_types_from_typevar(typevar: _TypeVar_) -> _TypeParameter | UnionParameter_

The `get_types_from_typevar` function returns the type constraints from the typevar. If no constraints are specified, `type[Any]` is returned.

## Other similar projects

There are other similar projects out there like [typing-utils](https://pypi.org/project/typing-utils/) and [runtype](https://pypi.org/project/runtype/), and while typing-utils is outdated and pretty basic, runtype is very similar to `typing-utilities` when it comes to validation.