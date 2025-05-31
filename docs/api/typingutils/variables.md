[Start](/README.md) > [API](/docs/api.md) > typingutils module variables
# `typingutils` module variables

## TypeParameter

The `TypeParameter` variable is an annotation of `type | type[Any]` and matches any ordinary type.

## TypeVarParameter

The `TypeVarParameter` variable is an annotation of `TypeVar | TypeVarTuple` and matches any generic typevar or variadic typevar tuple (new in python 3.11).

## UnionParameter

The `UnionParameter` variable is an annotation of `types.UnionType | tuple[TypeParameter, ...]` and matches any type union.

## AnyType

The `AnyType` variable is an annotation of `TypeParameter | UnionParameter | TypeVarParameter]` and matches any type, typevar or union.

## TypeArgs

The `TypeArgs` variable is an annotation of `tuple[AnyType, ...]` and matches any sequence of types, typevars or unions.

## AnyFunction

The `AnyFunction` Variable is an annotation of `types.FunctionType | typing.Callable[..., Any]`