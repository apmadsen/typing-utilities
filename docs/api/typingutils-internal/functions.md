[API](/docs/api.md) > typingutils.internal module functions
# `typingutils.internal` module functions

## get_generic_origin(cls: _AnyType_) -> _TypeParameter_

The `get_generic_origin` function returns the generic origin of a type i.e. the type a generic type originates from.

## get_union_types(cls: _UnionParameter_) -> _TypeParameter_

The `get_union_types` function returns the types which make up the specified union.

## get_original_class(cls: _AnyType_) -> _TypeParameter_

The `get_original_class` function returns the original generic type from a class instance. This is useful for generic types because instances of these doesn't derive from them, thus having no generic arguments specified. Will even work when called from within a constructor of a class. Note that it doesn't work with builtin generic types like list[T].

## get_types_from_typevar(typevar: _TypeVarParameter_) -> _TypeParameter | UnionParameter_

The `get_types_from_typevar` function returns the type constraints from the typevar or typevar tuple. If no constraints are specified, `type[Any]` is returned.

If typevar is a TypeVarTuple (new in Python 3.11), `tuple[type[Any], ...]` is returned..

## get_executing_function() -> _AnyFunction | None_

The `get_executing_function` function returns the executing function from within, enabling retrieval of its generic parameters via the `get_generic_parameters` function.
